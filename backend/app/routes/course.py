"""
Course routes
"""

from flask import Blueprint

bp = Blueprint('course', __name__, url_prefix='/courses')


@bp.route('/')
def list_courses():
    """List courses"""
    pass
