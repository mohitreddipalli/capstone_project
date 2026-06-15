"""
Course routes
"""

from flask import Blueprint, render_template
from app.utils.decorators import login_required

bp = Blueprint('course', __name__, url_prefix='/courses')


@bp.route('/')
@login_required
def list_courses():
    """List courses"""
    return render_template('course/courses_list.html')


@bp.route('/my-courses')
@login_required
def my_courses():
    """Current user's courses"""
    return render_template('course/my_courses.html')
