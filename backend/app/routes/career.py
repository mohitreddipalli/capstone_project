"""
Career routes
"""

from flask import Blueprint, render_template
from app.utils.decorators import login_required

bp = Blueprint('career', __name__, url_prefix='/career')


@bp.route('/analysis')
@login_required
def analysis():
    """Career analysis"""
    return render_template('career/analysis.html')
