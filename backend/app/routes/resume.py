"""
Resume routes
"""

from flask import Blueprint, jsonify, request
from app.utils.decorators import login_required

bp = Blueprint('resume', __name__, url_prefix='/resume')


@bp.route('/upload', methods=['POST'])
@login_required
def upload():
    """Upload resume"""
    if 'resume' not in request.files:
        return jsonify({'status': False, 'message': 'No resume file uploaded'}), 400
    return jsonify({'status': True, 'message': 'Resume upload endpoint is ready'})
