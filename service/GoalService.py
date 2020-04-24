from model.Goal import GoalRequest
from repository.GoalRepository import GoalRepository


class GoalService:
    def __init__(self):
        self.goal_repository = GoalRepository()

    def create_goal(self, goal_request: GoalRequest):
        row_id = self.goal_repository.insert(**goal_request.__dict__)
        return row_id

    def update_goal(self, goal_id: int, goal_request: GoalRequest):
        goal = self.goal_repository.find_by(goal_id=goal_id)
        if goal is not None:
            request = dict()
            request['goal_id'] = goal_id
            if goal_request.status is not None:
                request['status'] = goal_request.status
            self.goal_repository.update(**request)
