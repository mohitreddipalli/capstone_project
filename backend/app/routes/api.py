"""
API routes
"""

from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/health')
def health():
    """Health check"""
    return jsonify({'status': 'healthy', 'message': 'AI Career Platform is running'})
