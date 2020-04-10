from model.Goal import GoalRequest
from repository.GoalRepository import GoalRepository


class GoalService:
    def __init__(self):
        self.goal_repository = GoalRepository()

    def create_goal(self, goal_request: GoalRequest):
        row_id = self.goal_repository.insert(**goal_request.__dict__)
        return row_id
