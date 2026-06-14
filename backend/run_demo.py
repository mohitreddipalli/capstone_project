"""
Run script for AI Career Development Platform
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Flask environment
os.environ['FLASK_ENV'] = os.getenv('FLASK_ENV', 'development')
os.environ['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG', 'True')

# Simple Flask app for demo
from flask import Flask, render_template, redirect, url_for, session, request, g
from datetime import timedelta
import functools

# Create Flask app
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=14)

# Demo user storage
DEMO_USERS = {}

@app.before_request
def load_user():
    """Load user from session if exists"""
    g.user = None
    if 'user_id' in session:
        user_id = session['user_id']
        if user_id in DEMO_USERS:
            g.user = DEMO_USERS[user_id].copy()

@app.context_processor
def inject_user():
    """Inject user into templates"""
    return {
        'user': g.user,
        'request': request
    }

def login_required(f):
    """Decorator to require login"""
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        
        # Simple validation
        if not all([username, email, password, first_name, last_name]):
            return render_template('auth/register.html', error='All fields required'), 400
        
        if len(password) < 8:
            return render_template('auth/register.html', error='Password must be at least 8 characters'), 400
        
        if email in [u['email'] for u in DEMO_USERS.values()]:
            return render_template('auth/register.html', error='Email already registered'), 400
        
        # Store user
        user_id = len(DEMO_USERS) + 1
        DEMO_USERS[user_id] = {
            'id': user_id,
            'username': username,
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'verified': False
        }
        
        # Show OTP verification (demo: OTP is always 123456)
        session['temp_user_id'] = user_id
        return redirect(url_for('verify_otp'))
    
    return render_template('auth/register.html')

@app.route('/auth/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    """Verify OTP"""
    if 'temp_user_id' not in session:
        return redirect(url_for('register'))
    
    if request.method == 'POST':
        otp = request.form.get('otp', '')
        # Demo: always accept OTP 123456
        if otp == '123456' or True:  # Accept any OTP for demo
            user_id = session.pop('temp_user_id')
            DEMO_USERS[user_id]['verified'] = True
            return redirect(url_for('login'))
        else:
            return render_template('auth/verify_otp.html', error='Invalid OTP'), 400
    
    return render_template('auth/verify_otp.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        
        # Find user
        user = None
        for u in DEMO_USERS.values():
            if u['email'] == email and u['password'] == password:
                user = u
                break
        
        if not user:
            return render_template('auth/login.html', error='Invalid email or password'), 401
        
        if not user['verified']:
            session['temp_user_id'] = user['id']
            return redirect(url_for('verify_otp'))
        
        # Set session
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['first_name'] = user['first_name']
        session['email'] = user['email']
        session.permanent = True
        
        return redirect(url_for('dashboard'))
    
    return render_template('auth/login.html')

@app.route('/auth/logout')
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('home'))

@app.route('/user/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    return render_template('user/dashboard.html')

@app.route('/user/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('user/profile.html')

@app.route('/user/settings')
@login_required
def settings():
    """User settings page"""
    return render_template('user/settings.html')

@app.route('/user/resume')
@login_required
def resume():
    """Resume management page"""
    return render_template('user/resume.html')

@app.route('/career/analysis')
@login_required
def career_analysis():
    """Career analysis page"""
    return render_template('career/analysis.html')

@app.route('/jobs')
@login_required
def jobs_list():
    """Job board page"""
    return render_template('job/jobs_list.html')

@app.route('/jobs/saved')
@login_required
def saved_jobs():
    """Saved jobs page"""
    return render_template('job/saved_jobs.html')

@app.route('/jobs/applications')
@login_required
def job_applications():
    """Job applications page"""
    return render_template('job/applications.html')

@app.route('/courses')
@login_required
def courses_list():
    """Course catalog page"""
    return render_template('course/courses_list.html')

@app.route('/courses/my-courses')
@login_required
def my_courses():
    """My courses page"""
    return render_template('course/my_courses.html')

@app.route('/analytics')
@login_required
def analytics():
    """Analytics dashboard"""
    return render_template('analytics/dashboard.html')

# AJAX API Endpoints for Search and Filtering
@app.route('/api/jobs/search')
@login_required
def api_search_jobs():
    """Search jobs with filters"""
    search_term = request.args.get('q', '')
    job_type = request.args.get('type', '')
    experience = request.args.get('experience', '')
    location = request.args.get('location', '')
    
    # Demo jobs data
    demo_jobs = [
        {
            'id': 1,
            'title': 'Senior Full Stack Developer',
            'company': 'Tech Innovations Inc.',
            'location': 'San Francisco, CA',
            'salary_min': 120000,
            'salary_max': 160000,
            'match': 92,
            'type': 'full-time',
            'experience': 'senior',
            'skills': ['Python', 'React', 'AWS']
        },
        {
            'id': 2,
            'title': 'Machine Learning Engineer',
            'company': 'AI Solutions Corp',
            'location': 'Remote',
            'salary_min': 130000,
            'salary_max': 180000,
            'match': 88,
            'type': 'full-time',
            'experience': 'senior',
            'skills': ['Python', 'TensorFlow', 'ML']
        },
        {
            'id': 3,
            'title': 'Frontend Developer',
            'company': 'Web Design Studios',
            'location': 'New York, NY',
            'salary_min': 90000,
            'salary_max': 130000,
            'match': 85,
            'type': 'full-time',
            'experience': 'mid',
            'skills': ['React', 'JavaScript', 'CSS']
        }
    ]
    
    # Filter based on search parameters
    results = demo_jobs
    if search_term:
        results = [j for j in results if search_term.lower() in j['title'].lower() or search_term.lower() in j['company'].lower()]
    if job_type:
        results = [j for j in results if j['type'] == job_type]
    if experience:
        results = [j for j in results if j['experience'] == experience]
    if location:
        results = [j for j in results if location.lower() in j['location'].lower()]
    
    return {'success': True, 'jobs': results, 'total': len(results)}

@app.route('/api/courses/search')
@login_required
def api_search_courses():
    """Search courses with filters"""
    search_term = request.args.get('q', '')
    category = request.args.get('category', '')
    level = request.args.get('level', '')
    
    # Demo courses data
    demo_courses = [
        {
            'id': 1,
            'name': 'Complete Python Bootcamp',
            'category': 'web',
            'level': 'beginner',
            'rating': 4.8,
            'price': 49.99,
            'hours': 40
        },
        {
            'id': 2,
            'name': 'React.js Masterclass',
            'category': 'web',
            'level': 'intermediate',
            'rating': 4.7,
            'price': 59.99,
            'hours': 35
        },
        {
            'id': 3,
            'name': 'Machine Learning Fundamentals',
            'category': 'ml',
            'level': 'intermediate',
            'rating': 4.6,
            'price': 69.99,
            'hours': 50
        },
        {
            'id': 4,
            'name': 'AWS Solutions Architect',
            'category': 'cloud',
            'level': 'advanced',
            'rating': 4.5,
            'price': 79.99,
            'hours': 45
        }
    ]
    
    # Filter based on search parameters
    results = demo_courses
    if search_term:
        results = [c for c in results if search_term.lower() in c['name'].lower()]
    if category:
        results = [c for c in results if c['category'] == category]
    if level:
        results = [c for c in results if c['level'] == level]
    
    return {'success': True, 'courses': results, 'total': len(results)}

@app.route('/api/apply-job', methods=['POST'])
@login_required
def api_apply_job():
    """Apply for a job"""
    job_id = request.json.get('job_id')
    cover_letter = request.json.get('cover_letter', '')
    
    return {'success': True, 'message': 'Application submitted successfully!', 'application_id': 123}

@app.route('/api/enroll-course', methods=['POST'])
@login_required
def api_enroll_course():
    """Enroll in a course"""
    course_id = request.json.get('course_id')
    
    return {'success': True, 'message': 'Enrolled successfully!', 'enrollment_id': 456}

@app.route('/api/save-job', methods=['POST'])
@login_required
def api_save_job():
    """Save a job"""
    job_id = request.json.get('job_id')
    
    return {'success': True, 'message': 'Job saved!'}

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'message': 'AI Career Platform is running!'}

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('error.html', error_code=404, message='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('error.html', error_code=500, message='Internal server error'), 500

if __name__ == '__main__':
    # Get environment settings
    flask_env = os.getenv('FLASK_ENV', 'development')
    debug_mode = os.getenv('DEBUG', 'True').lower() == 'true'
    port = int(os.getenv('PORT', 5000))
    
    # Only show banner in development
    if flask_env == 'development':
        print("\n" + "="*60)
        print("🚀 AI Career Development Platform")
        print("="*60)
        print("\n✅ Demo Mode (No Database Required)")
        print("\n📝 Test Credentials:")
        print("   Email: demo@example.com (after registration)")
        print("   OTP: Any 6-digit code (demo accepts all)")
        print(f"\n🌐 Server: http://localhost:{port}")
        print(f"   Home: http://localhost:{port}/")
        print(f"   Register: http://localhost:{port}/auth/register")
        print(f"   Login: http://localhost:{port}/auth/login")
        print(f"   Dashboard: http://localhost:{port}/user/dashboard")
        print("\n💡 Stop server: Press Ctrl+C")
        print("="*60 + "\n")
    
    # Run server
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode,
        use_reloader=debug_mode
    )
