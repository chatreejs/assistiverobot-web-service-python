from flask import Blueprint, jsonify, abort, request
from kanpai import Kanpai

from model.Goal import GoalRequest, GoalStatus
from service.GoalService import GoalService

goal_controller = Blueprint('goal_controller', __name__)
goal_service = GoalService()


@goal_controller.route('/api/v1/goals/<int:goal_id>', methods=['PATCH'])
def update_goal_by_id(goal_id):
    schema = Kanpai.Object({
        'status': Kanpai.String().required()
    })
    validation_result = schema.validate(request.json)
    if validation_result.get('success', False) is False:
        abort(400)

    if request.json['status'] is not None:
        status_mapping = dict((item.value, item) for item in GoalStatus)
        if request.json['status'] not in status_mapping:
            abort(400)

    goal = GoalRequest(job_id=None,
                       position_x=None,
                       position_y=None,
                       position_z=None,
                       orientation_x=None,
                       orientation_y=None,
                       orientation_z=None,
                       orientation_w=None,
                       status=request.json['status'])

    try:
        goal_service.update_goal(goal_id, goal)
        return jsonify(message='success')
    except ValueError as e:
        abort(400)
    except Exception as e:
        print(e)
        abort(500)
