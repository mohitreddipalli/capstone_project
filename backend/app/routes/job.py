"""
Job routes
"""

from flask import Blueprint

bp = Blueprint('job', __name__, url_prefix='/jobs')


@bp.route('/')
def list_jobs():
    """List jobs"""
    pass
