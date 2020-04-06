class Goal:
    def __init__(self, position: dict, orientation: dict):
        self.position = position
        self.orientation = orientation


class Position:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Orientation:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
