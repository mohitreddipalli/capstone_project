"""
Authentication routes
"""

from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from app.services.auth_service import AuthService
from app.utils.decorators import login_required
from app.utils.helpers import get_db

# Create blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    """Load user from session before each request"""
    user_id = session.get('user_id')
    if user_id is None:
        user = None
    else:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
    
    from flask import g
    g.user = user


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        
        # Validate
        if not all([username, email, password, confirm_password]):
            return render_template('auth/register.html', error='All fields are required'), 400
        
        if password != confirm_password:
            return render_template('auth/register.html', error='Passwords do not match'), 400
        
        # Register user
        result = AuthService.register_user(username, email, password, first_name, last_name)
        
        if not result['status']:
            return render_template('auth/register.html', error=result['message']), 400
        
        # Redirect to OTP verification
        session['user_id'] = result['user_id']
        session['email'] = email
        return redirect(url_for('auth.verify_otp'))
    
    return render_template('auth/register.html')


@bp.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    """Verify OTP"""
    if 'user_id' not in session:
        return redirect(url_for('auth.register'))
    
    if request.method == 'POST':
        otp = request.form.get('otp', '').strip()
        
        if not otp or len(otp) != 6:
            error = 'Please enter a valid 6-digit OTP'
            return render_template('auth/verify_otp.html', error=error, email=session.get('email')), 400
        
        # Verify OTP
        result = AuthService.verify_otp(session['user_id'], otp)
        
        if not result['status']:
            return render_template('auth/verify_otp.html', error=result['message'], email=session.get('email')), 400
        
        # Clear session and redirect to login
        session.clear()
        return redirect(url_for('auth.login'))
    
    return render_template('auth/verify_otp.html', email=session.get('email'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        if not email or not password:
            return render_template('auth/login.html', error='Email and password are required'), 400
        
        # Authenticate
        result = AuthService.login_user(email, password)
        
        if not result['status']:
            return render_template('auth/login.html', error=result['message']), 401
        
        # Set session
        user = result['user']
        session.clear()
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['email'] = user['email']
        session['role'] = user['role']
        session.permanent = True
        
        # Redirect based on role
        if user['role'] == 'admin':
            return redirect(url_for('admin.dashboard'))
        else:
            return redirect(url_for('user.dashboard'))
    
    return render_template('auth/login.html')


@bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Forgot password - initiate reset"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        
        if not email:
            return render_template('auth/forgot_password.html', error='Email is required'), 400
        
        # Initiate password reset
        result = AuthService.initiate_password_reset(email)
        
        # Always show success message (security best practice)
        return render_template('auth/forgot_password.html', 
                             message='If the email exists in our system, a password reset link has been sent',
                             success=True)
    
    return render_template('auth/forgot_password.html')


@bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Reset password with token"""
    if request.method == 'POST':
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        if not password or not confirm_password:
            return render_template('auth/reset_password.html', error='All fields are required', token=token), 400
        
        if password != confirm_password:
            return render_template('auth/reset_password.html', error='Passwords do not match', token=token), 400
        
        # Reset password
        result = AuthService.reset_password(token, password)
        
        if not result['status']:
            return render_template('auth/reset_password.html', error=result['message'], token=token), 400
        
        # Redirect to login
        return redirect(url_for('auth.login'))
    
    return render_template('auth/reset_password.html', token=token)


@bp.route('/logout')
@login_required
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('auth.login'))


@bp.route('/resend-otp', methods=['POST'])
def resend_otp():
    """Resend OTP via AJAX"""
    if 'user_id' not in session:
        return jsonify({'status': False, 'message': 'Session expired'}), 401
    
    user_id = session['user_id']
    email = session.get('email')
    
    if not email:
        return jsonify({'status': False, 'message': 'Email not found'}), 400
    
    try:
        from app.utils.helpers import generate_otp, hash_password
        from app.services.email_service import EmailService
        from flask import current_app
        from datetime import datetime, timedelta
        
        # Generate new OTP
        otp = '123456' if current_app.config.get('DEBUG') else generate_otp()
        otp_hash = hash_password(otp)
        expiry_time = datetime.now() + timedelta(minutes=current_app.config['OTP_EXPIRY'])
        
        db = get_db()
        cursor = db.cursor()
        
        # Insert new OTP record
        cursor.execute(
            """
            INSERT INTO otp_verifications (user_id, otp, email, purpose, expires_at)
            VALUES (%s, %s, %s, 'registration', %s)
            """,
            (user_id, otp_hash, email, expiry_time)
        )
        db.commit()
        
        # Send email
        EmailService.send_verification_email(email, otp)
        
        return jsonify({'status': True, 'message': 'OTP resent successfully'})
    
    except Exception as e:
        return jsonify({'status': False, 'message': 'Failed to resend OTP'}), 500
