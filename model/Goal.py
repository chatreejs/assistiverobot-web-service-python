class Goal(object):
    def __init__(self, position: dict, orientation: dict):
        self.position = position
        self.orientation = orientation


class GoalRequest(object):
    def __init__(self, job_id: int, position_x: float, position_y: float, position_z: float, orientation_x: float,
                 orientation_y: float, orientation_z: float, orientation_w: float):
        self.job_id = job_id
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.orientation_x = orientation_x
        self.orientation_y = orientation_y
        self.orientation_z = orientation_z
        self.orientation_w = orientation_w


class Position(object):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Orientation(object):
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
