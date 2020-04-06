from repository.BaseRepository import BaseRepository


class JobRepository(BaseRepository):
    def __init__(self):
        super().__init__(table='jobs')
