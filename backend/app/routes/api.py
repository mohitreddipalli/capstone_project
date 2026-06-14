"""
API routes
"""

from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/health')
def health():
    """Health check"""
    pass
