"""
Career routes
"""

from flask import Blueprint

bp = Blueprint('career', __name__, url_prefix='/career')


@bp.route('/analysis')
def analysis():
    """Career analysis"""
    pass
