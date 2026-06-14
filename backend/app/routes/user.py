"""
User routes
"""

from flask import Blueprint, render_template
from app.utils.decorators import login_required

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    return render_template('user/dashboard.html')


@bp.route('/profile')
@login_required
def profile():
    """User profile"""
    return render_template('user/profile.html')
