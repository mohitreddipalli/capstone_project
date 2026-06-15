"""
Configuration file for AI Career Development Platform
"""

import os
from dotenv import load_dotenv
from datetime import timedelta

BASE_DIR = os.path.dirname(__file__)

# Load environment variables from the project root and backend/.env.
load_dotenv()
load_dotenv(os.path.join(BASE_DIR, '.env'), override=False)


def env_bool(name, default=False):
    """Read a boolean environment variable safely."""
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 'yes', 'on'}


class Config:
    """Base configuration"""
    
    # Flask Settings
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = env_bool('FLASK_DEBUG', True)
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    APP_URL = os.getenv('APP_URL', 'http://localhost:5000')
    
    # Database Configuration
    DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite').lower()
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///ai_career.db')
    SQLITE_DB_PATH = os.getenv('SQLITE_DB_PATH', os.path.join(BASE_DIR, 'ai_career.db'))
    MYSQL_HOST = os.getenv('DB_HOST', 'localhost')
    MYSQL_USER = os.getenv('DB_USER', 'root')
    MYSQL_PASSWORD = os.getenv('DB_PASSWORD', '')
    MYSQL_DB = os.getenv('DB_NAME', 'ai_career_db')
    MYSQL_PORT = int(os.getenv('DB_PORT', 3306))
    MYSQL_CURSORCLASS = 'DictCursor'
    
    # Session Configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)
    SESSION_COOKIE_SECURE = env_bool('SESSION_COOKIE_SECURE', False)
    SESSION_COOKIE_HTTPONLY = env_bool('SESSION_COOKIE_HTTPONLY', True)
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')
    
    # Email Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = env_bool('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    
    # OpenAI API
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Upload Configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    ALLOWED_RESUME_EXTENSIONS = {'pdf'}
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16777216))  # 16MB
    
    # Security
    CSRF_ENABLED = env_bool('CSRF_ENABLED', True)
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key-change-in-production')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
    
    # Token Expiry
    PASSWORD_RESET_TOKEN_EXPIRY = int(os.getenv('PASSWORD_RESET_TOKEN_EXPIRY', 24))  # hours
    OTP_EXPIRY = int(os.getenv('OTP_EXPIRY', 10))  # minutes
    
    # Pagination
    ITEMS_PER_PAGE = int(os.getenv('ITEMS_PER_PAGE', 10))
    
    # AI Settings
    MIN_RESUME_SCORE = int(os.getenv('MIN_RESUME_SCORE', 0))
    MAX_RESUME_SCORE = int(os.getenv('MAX_RESUME_SCORE', 100))
    SKILL_GAP_THRESHOLD = int(os.getenv('SKILL_GAP_THRESHOLD', 70))


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    MYSQL_DB = 'ai_career_test_db'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
