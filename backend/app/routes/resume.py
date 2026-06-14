"""
Resume routes
"""

from flask import Blueprint

bp = Blueprint('resume', __name__, url_prefix='/resume')


@bp.route('/upload', methods=['POST'])
def upload():
    """Upload resume"""
    pass
