class Goal(object):
    def __init__(self, position: dict, quaternion: dict):
        self.position = position
        self.quaternion = quaternion


class GoalRequest(object):
    def __init__(self, job_id: int, position_x: float, position_y: float, position_z: float, quaternion_x: float,
                 quaternion_y: float, quaternion_z: float, quaternion_w: float):
        self.job_id = job_id
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.quaternion_x = quaternion_x
        self.quaternion_y = quaternion_y
        self.quaternion_z = quaternion_z
        self.quaternion_w = quaternion_w


class Position(object):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Quaternion(object):
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
