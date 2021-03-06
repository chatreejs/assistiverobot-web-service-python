from flask import Flask, jsonify
from flask_cors import CORS

from controller.GoalController import goal_controller
from controller.JobController import job_controller

application = Flask(__name__)
application.config['JSON_SORT_KEYS'] = False
CORS(application, resources={r"/api/*": {"origins": "*"}})

application.register_blueprint(job_controller)
application.register_blueprint(goal_controller)


@application.errorhandler(400)
def bad_request(error):
    return jsonify(message='bad request', result=None), 400


@application.errorhandler(404)
def not_found(error):
    return jsonify(message='not found', result=None), 404


@application.errorhandler(500)
def internal_error(error):
    return jsonify(message='internal server error', result=None), 500


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
