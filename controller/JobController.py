from flask import Blueprint, jsonify, abort

from service.JobService import JobService

job_controller = Blueprint('deed_controller', __name__)
job_service = JobService()


@job_controller.route('/api/v1/jobs', methods=['GET'])
def get_jobs():
    jobs = job_service.get_jobs()
    if jobs is None:
        return jsonify({}), 204
    return jsonify(message='success', result=jobs), 200


@job_controller.route('/api/v1/jobs/<int:job_id>', methods=['GET'])
def get_job_by_id(job_id):
    jobs = job_service.get_jobs_by(job_id=job_id)
    if jobs is None:
        abort(404)
    return jsonify(message='success', result=jobs), 200
