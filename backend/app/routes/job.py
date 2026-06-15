"""
Job routes
"""

from flask import Blueprint, render_template
from app.utils.decorators import login_required

bp = Blueprint('job', __name__, url_prefix='/jobs')


@bp.route('/')
@login_required
def list_jobs():
    """List jobs"""
    return render_template('job/jobs_list.html')


@bp.route('/saved')
@login_required
def saved_jobs():
    """Saved jobs"""
    return render_template('job/saved_jobs.html')


@bp.route('/applications')
@login_required
def applications():
    """Job applications"""
    return render_template('job/applications.html')
