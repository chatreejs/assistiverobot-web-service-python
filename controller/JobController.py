from flask import Blueprint, jsonify

from service.JobService import JobService

job_controller = Blueprint('deed_controller', __name__)
job_service = JobService()


@job_controller.route('/api/v1/jobs', methods=['GET'])
def get_jobs():
    jobs = job_service.get_jobs()
    if jobs is None:
        return jsonify({}), 204
    return jsonify(message='success', result=jobs), 200
