"""
Admin routes
"""

from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/dashboard')
def dashboard():
    """Admin dashboard"""
    pass
