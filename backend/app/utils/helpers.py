"""
Helper functions for common operations
"""

import os
import sqlite3
from urllib.parse import urlparse
from flask import g, current_app
import hashlib
import secrets
import string
from datetime import datetime, timedelta

try:
    import MySQLdb
except ImportError:
    MySQLdb = None


class SQLiteCursor:
    """Tiny cursor adapter so existing MySQL-style queries run on SQLite."""

    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query, params=()):
        query = query.replace('%s', '?')
        self.cursor.execute(query, params)
        return self

    def fetchone(self):
        row = self.cursor.fetchone()
        return dict(row) if row is not None else None

    def fetchall(self):
        return [dict(row) for row in self.cursor.fetchall()]

    @property
    def lastrowid(self):
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()


class SQLiteConnection:
    """Connection adapter that returns dict-like rows."""

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row

    def cursor(self):
        return SQLiteCursor(self.connection.cursor())

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.connection.close()


def _sqlite_path():
    database_url = current_app.config.get('DATABASE_URL', '')
    if database_url.startswith('sqlite:///'):
        parsed_path = urlparse(database_url).path.lstrip('/')
        if parsed_path and parsed_path != ':memory:':
            return os.path.join(os.path.dirname(current_app.root_path), parsed_path)
    return current_app.config['SQLITE_DB_PATH']


def get_db():
    """Get a database connection."""
    if 'db' not in g:
        if current_app.config.get('DATABASE_TYPE') == 'sqlite':
            db_path = _sqlite_path()
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            g.db = SQLiteConnection(db_path)
        else:
            if MySQLdb is None:
                raise RuntimeError('MySQLdb is not installed. Use DATABASE_TYPE=sqlite or install mysqlclient.')
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


def init_sqlite_db(app):
    """Create the local SQLite schema and starter content."""
    if app.config.get('DATABASE_TYPE') != 'sqlite':
        return

    db_path = app.config['SQLITE_DB_PATH']
    database_url = app.config.get('DATABASE_URL', '')
    if database_url.startswith('sqlite:///'):
        parsed_path = urlparse(database_url).path.lstrip('/')
        if parsed_path and parsed_path != ':memory:':
            db_path = os.path.join(os.path.dirname(app.root_path), parsed_path)
            app.config['SQLITE_DB_PATH'] = db_path

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    connection = sqlite3.connect(db_path)
    try:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                first_name TEXT,
                last_name TEXT,
                phone TEXT,
                location TEXT,
                headline TEXT,
                bio TEXT,
                profile_image TEXT,
                role TEXT DEFAULT 'user',
                is_verified INTEGER DEFAULT 0,
                is_active INTEGER DEFAULT 1,
                reset_token TEXT,
                reset_token_expiry TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS otp_verifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                otp TEXT NOT NULL,
                email TEXT NOT NULL,
                purpose TEXT DEFAULT 'registration',
                is_used INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL UNIQUE,
                file_path TEXT NOT NULL,
                file_name TEXT NOT NULL,
                file_size INTEGER,
                original_text TEXT,
                parsed_data TEXT,
                resume_score REAL,
                extracted_skills TEXT,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT NOT NULL,
                company_name TEXT NOT NULL,
                description TEXT NOT NULL,
                requirements TEXT,
                salary_min REAL,
                salary_max REAL,
                currency TEXT DEFAULT 'USD',
                location TEXT,
                job_type TEXT DEFAULT 'full-time',
                experience_level TEXT DEFAULT 'mid',
                skills_required TEXT,
                is_active INTEGER DEFAULT 1,
                posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                description TEXT,
                course_level TEXT DEFAULT 'intermediate',
                instructor_name TEXT,
                duration_hours INTEGER,
                category TEXT,
                skills_taught TEXT,
                certification_available INTEGER DEFAULT 1,
                is_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS job_applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                job_id INTEGER NOT NULL,
                application_status TEXT DEFAULT 'applied',
                cover_letter TEXT,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, job_id)
            );

            CREATE TABLE IF NOT EXISTS saved_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                job_id INTEGER NOT NULL,
                saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, job_id)
            );
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO users
            (id, username, email, password_hash, first_name, last_name, role, is_verified, is_active)
            VALUES (1, 'demo', 'demo@example.com', ?, 'Demo', 'User', 'user', 1, 1)
            """,
            (hash_password('Demo@123'),)
        )
        connection.executemany(
            """
            INSERT OR IGNORE INTO jobs
            (id, job_title, company_name, description, location, job_type, experience_level, salary_min, salary_max, skills_required)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (1, 'Full Stack Developer', 'Tech Innovations Inc.', 'Build modern web applications with Python and JavaScript.', 'Remote', 'full-time', 'mid', 90000, 130000, 'Python, Flask, JavaScript'),
                (2, 'Machine Learning Engineer', 'AI Solutions Corp', 'Develop ML workflows and production AI features.', 'Bengaluru', 'full-time', 'senior', 120000, 170000, 'Python, ML, TensorFlow'),
            ]
        )
        connection.executemany(
            """
            INSERT OR IGNORE INTO courses
            (id, course_name, description, course_level, instructor_name, duration_hours, category, skills_taught)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (1, 'Complete Python Bootcamp', 'Python fundamentals through practical backend projects.', 'beginner', 'AI Career Team', 40, 'Programming', 'Python, Flask'),
                (2, 'Machine Learning Fundamentals', 'Core ML concepts, model training, and evaluation.', 'intermediate', 'AI Career Team', 50, 'AI/ML', 'Python, Machine Learning'),
            ]
        )
        connection.commit()
    finally:
        connection.close()


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
