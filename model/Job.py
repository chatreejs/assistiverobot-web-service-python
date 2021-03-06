import datetime
from enum import Enum

from model import Goal


class JobStatus(Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAILED = 'failed'


class JobResponse(object):
    def __init__(self, job_id: int, goal: [Goal], status: str, created_date: datetime, updated_date: datetime):
        self.job_id = job_id
        self.goal = goal
        self.status = status
        self.created_date = created_date
        self.updated_date = updated_date


class JobRequest(object):
    def __init__(self, status: str, created_date: datetime, updated_date: datetime):
        self.status = status
        self.created_date = created_date
        self.updated_date = updated_date
