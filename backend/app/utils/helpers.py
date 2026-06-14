"""
Helper functions for common operations
"""

import MySQLdb
from flask import g, current_app
import hashlib
import secrets
import string
from datetime import datetime, timedelta


def get_db():
    """Get MySQL database connection"""
    if 'db' not in g:
        g.db = MySQLdb.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            passwd=current_app.config['MYSQL_PASSWORD'],
            db=current_app.config['MYSQL_DB'],
            port=current_app.config['MYSQL_PORT'],
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8mb4'
        )
    return g.db


def close_db(e=None):
    """Close database connection"""
    db = g.pop('db', None)
    if db is not None:
        db.close()


def hash_password(password):
    """
    Hash password using SHA256
    
    Args:
        password: Plain text password
    
    Returns:
        Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed_password):
    """
    Verify password against hash
    
    Args:
        password: Plain text password
        hashed_password: Hashed password
    
    Returns:
        True if password matches, False otherwise
    """
    return hash_password(password) == hashed_password


def generate_otp(length=6):
    """
    Generate random OTP
    
    Args:
        length: OTP length
    
    Returns:
        Random OTP string
    """
    digits = string.digits
    return ''.join(secrets.choice(digits) for _ in range(length))


def generate_token(length=32):
    """
    Generate random token
    
    Args:
        length: Token length
    
    Returns:
        Random token string
    """
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


def is_otp_expired(created_at, expiry_minutes):
    """
    Check if OTP has expired
    
    Args:
        created_at: OTP creation time
        expiry_minutes: Expiry time in minutes
    
    Returns:
        True if expired, False otherwise
    """
    return datetime.now() > created_at + timedelta(minutes=expiry_minutes)


def format_currency(amount, currency='USD'):
    """
    Format amount as currency
    
    Args:
        amount: Amount to format
        currency: Currency code
    
    Returns:
        Formatted currency string
    """
    if currency == 'USD':
        return f"${amount:,.2f}"
    return f"{currency} {amount:,.2f}"


def paginate(page, per_page=10, total=None):
    """
    Calculate pagination offsets
    
    Args:
        page: Current page number
        per_page: Items per page
        total: Total items (optional)
    
    Returns:
        Dictionary with pagination info
    """
    if page < 1:
        page = 1
    
    offset = (page - 1) * per_page
    
    result = {
        'page': page,
        'per_page': per_page,
        'offset': offset
    }
    
    if total:
        result['total'] = total
        result['total_pages'] = (total + per_page - 1) // per_page
        result['has_prev'] = page > 1
        result['has_next'] = page < result['total_pages']
    
    return result


def get_user_from_session(user_id):
    """
    Get user from database using session user_id
    
    Args:
        user_id: User ID from session
    
    Returns:
        User dictionary or None
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id, username, email, first_name, last_name, 
               role, is_verified, profile_image 
        FROM users WHERE id = %s AND is_active = TRUE
        """,
        (user_id,)
    )
    user = cursor.fetchone()
    cursor.close()
    return user


def is_valid_email(email):
    """
    Validate email format
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_strong_password(password):
    """
    Check if password meets strength requirements
    
    Args:
        password: Password to check
    
    Returns:
        True if strong, False otherwise
    """
    # At least 8 characters, 1 uppercase, 1 lowercase, 1 digit, 1 special char
    import re
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        return False
    return True


def sanitize_filename(filename):
    """
    Sanitize filename for safe storage
    
    Args:
        filename: Original filename
    
    Returns:
        Sanitized filename
    """
    import os
    import uuid
    # Get file extension
    _, ext = os.path.splitext(filename)
    # Generate unique filename
    return f"{uuid.uuid4().hex}{ext}"


def allowed_file(filename, allowed_extensions):
    """
    Check if file extension is allowed
    
    Args:
        filename: Filename to check
        allowed_extensions: Set of allowed extensions
    
    Returns:
        True if allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
