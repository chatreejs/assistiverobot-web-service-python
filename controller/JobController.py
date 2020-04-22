import datetime

from flask import Blueprint, jsonify, abort, request
from kanpai import Kanpai

from model.Object import Object
from model.Goal import GoalRequest, GoalStatus
from model.Job import JobStatus, JobRequest
from service.GoalService import GoalService
from service.JobService import JobService

job_controller = Blueprint('deed_controller', __name__)
job_service = JobService()
goal_service = GoalService()


@job_controller.route('/api/v1/jobs', methods=['GET'])
def get_jobs():
    schema = Kanpai.Object({
        'status': Kanpai.String(),
        'limit': Kanpai.String()
    })
    validation_result = schema.validate(request.args.to_dict())
    if validation_result.get('success', False) is False:
        abort(400)
    if len(request.args) == 0:
        jobs = job_service.get_jobs()
        if jobs is None:
            return jsonify({}), 204
        return jsonify(message='success', result=jobs), 200
    else:
        jobs = None
        try:
            jobs = job_service.get_jobs_by(**request.args.to_dict())
        except Exception as e:
            abort(404)
        if jobs is None or len(jobs) == 0:
            abort(404)
        return jsonify(message='success', result=jobs), 200


@job_controller.route('/api/v1/jobs', methods=['POST'])
def create_job():
    schema = Kanpai.Object({
        'goal': Kanpai.Array({
            'position': Kanpai.Object({
                'x': Kanpai.Number().required(),
                'y': Kanpai.Number().required(),
                'z': Kanpai.Number().required()
            }).required(),
            'orientation': Kanpai.Object({
                'x': Kanpai.Number().required(),
                'y': Kanpai.Number().required(),
                'z': Kanpai.Number().required(),
                'w': Kanpai.Number().required()
            }).required()
        }).max(2).min(2).required()
    })
    validation_result = schema.validate(request.json)
    if validation_result.get('success', False) is False:
        abort(400)

    # Initial status to pending
    status = JobStatus.PENDING.value
    # Initial goal status to pending
    goal_status = GoalStatus.PENDING.value
    # Initial created date to now
    created_date = datetime.datetime.now()

    job = JobRequest(status=status,
                     created_date=created_date,
                     updated_date=None)

    try:
        job_id = job_service.create_job(job)
        if job_id is None:
            abort(400)

        for goal in [Object(obj) for obj in request.json['goal']]:
            goal_request = GoalRequest(job_id=job_id,
                                       position_x=goal.position.x,
                                       position_y=goal.position.y,
                                       position_z=goal.position.z,
                                       orientation_x=goal.orientation.x,
                                       orientation_y=goal.orientation.y,
                                       orientation_z=goal.orientation.z,
                                       orientation_w=goal.orientation.w,
                                       status=goal_status)
            goal_service.create_goal(goal_request)
        return jsonify(message='success', result=None), 201
    except Exception as e:
        abort(500)


@job_controller.route('/api/v1/jobs/<int:job_id>', methods=['GET'])
def get_job_by_id(job_id):
    jobs = job_service.get_jobs_by(job_id=job_id)
    if jobs is None:
        abort(404)
    return jsonify(message='success', result=jobs), 200


@job_controller.route('/api/v1/jobs/<int:job_id>', methods=['PATCH'])
def update_job_by_id(job_id):
    schema = Kanpai.Object({
        'status': Kanpai.String().required()
    })
    validation_result = schema.validate(request.json)
    if validation_result.get('success', False) is False:
        abort(400)

    updated_date = datetime.datetime.now()

    if request.json['status'] is not None:
        status_mapping = dict((item.value, item) for item in JobStatus)
        if request.json['status'] not in status_mapping:
            abort(400)

    job = JobRequest(status=request.json['status'],
                     created_date=None,
                     updated_date=updated_date)

    try:
        job_service.update_job(job_id, job)
        return jsonify(message='success')
    except ValueError as e:
        abort(400)
    except Exception as e:
        abort(500)
