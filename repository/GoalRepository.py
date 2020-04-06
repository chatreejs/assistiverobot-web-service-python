from repository.BaseRepository import BaseRepository


class GoalRepository(BaseRepository):
    def __init__(self):
        super().__init__(table='goals')
