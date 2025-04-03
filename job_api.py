from flask import Blueprint, jsonify, make_response, request

from data import db_session
from data.jobs import Jobs

bp = Blueprint(
    'jobs_api',
    __name__,
)


@bp.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'collaborators', "user.name"))
                 for item in jobs]
        }
    )
