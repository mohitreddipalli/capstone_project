"""
Utility decorators for route protection and validation
"""

from functools import wraps
from flask import session, redirect, url_for, abort, request, jsonify
from app.utils.helpers import get_db


def login_required(f):
    """Decorator to require user login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'error': 'Unauthorized'}), 401
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Decorator to require admin role"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'error': 'Unauthorized'}), 401
            return redirect(url_for('auth.login'))
        
        # Check if user is admin
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT role FROM users WHERE id = %s", (session['user_id'],))
        result = cursor.fetchone()
        cursor.close()
        
        if not result or result['role'] != 'admin':
            abort(403)
        
        return f(*args, **kwargs)
    return decorated_function


def api_login_required(f):
    """Decorator for API endpoints requiring login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized', 'status': False}), 401
        return f(*args, **kwargs)
    return decorated_function


def api_admin_required(f):
    """Decorator for API endpoints requiring admin role"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized', 'status': False}), 401
        
        # Check if user is admin
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT role FROM users WHERE id = %s", (session['user_id'],))
        result = cursor.fetchone()
        cursor.close()
        
        if not result or result['role'] != 'admin':
            return jsonify({'error': 'Forbidden', 'status': False}), 403
        
        return f(*args, **kwargs)
    return decorated_function
