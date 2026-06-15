"""
Admin routes
"""

from flask import Blueprint, render_template
from app.utils.decorators import admin_required

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/dashboard')
@admin_required
def dashboard():
    """Admin dashboard"""
    return render_template('user/dashboard.html')
