"""
Flask Application Factory
Initializes and configures the Flask application
"""

from flask import Flask
from config import config
import os


def create_app(config_name=None):
    """
    Application factory function
    
    Args:
        config_name: Configuration environment (development, testing, production)
    
    Returns:
        Flask application instance
    """
    
    # Determine configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    # Create Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Register blueprints
    register_blueprints(app)
    
    # Initialize database connections
    init_db(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Register context processors
    register_context_processors(app)
    
    return app


def register_blueprints(app):
    """Register Flask blueprints for routes"""
    
    from app.routes import auth_bp, user_bp, resume_bp, career_bp, job_bp, course_bp, api_bp, admin_bp
    
    app.register_blueprint(auth_bp.bp)
    app.register_blueprint(user_bp.bp)
    app.register_blueprint(resume_bp.bp)
    app.register_blueprint(career_bp.bp)
    app.register_blueprint(job_bp.bp)
    app.register_blueprint(course_bp.bp)
    app.register_blueprint(api_bp.bp)
    app.register_blueprint(admin_bp.bp)


def init_db(app):
    """Initialize database connection"""
    # Database initialization will be done when routes are accessed
    pass


def register_error_handlers(app):
    """Register error handlers"""
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not Found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal Server Error'}, 500
    
    @app.errorhandler(403)
    def forbidden(error):
        return {'error': 'Forbidden'}, 403


def register_context_processors(app):
    """Register context processors for templates"""
    
    @app.context_processor
    def inject_config():
        return {
            'app_name': app.config.get('APP_NAME', 'AI Career Platform'),
            'flask_env': app.config.get('FLASK_ENV')
        }
