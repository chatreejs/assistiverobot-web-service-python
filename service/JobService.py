from model.Goal import Position, Goal, Orientation
from model.Job import JobResponse, JobRequest
from repository.GoalRepository import GoalRepository
from repository.JobRepository import JobRepository


class JobService:
    def __init__(self):
        self.job_repository = JobRepository()
        self.goal_repository = GoalRepository()

    def build_response(self, result):
        job_response_list = []
        if isinstance(result, list):
            job_list = result
        else:
            job_list = [result]

        for job in job_list:
            goal_response_list = []
            goal_list = self.goal_repository.find_by(job_id=job.job_id)
            for goal in goal_list:
                position = Position(x=goal.position_x,
                                    y=goal.position_y,
                                    z=goal.position_z)
                orientation = Orientation(x=goal.orientation_x,
                                          y=goal.orientation_y,
                                          z=goal.orientation_z,
                                          w=goal.orientation_w)
                goal_response_list.append(Goal(position=position.__dict__, orientation=orientation.__dict__))

            job_response_list.append(
                JobResponse(job_id=job.job_id,
                            goal=[goal.__dict__ for goal in goal_response_list],
                            status=job.status,
                            created_date=job.created_date,
                            updated_date=job.updated_date))
        if len(job_response_list) == 1:
            return job_response_list[0].__dict__
        else:
            return [job.__dict__ for job in job_response_list]

    def get_jobs(self):
        result = self.job_repository.find_all()
        if result is not None:
            return self.build_response(result)
        else:
            return None

    def get_jobs_by(self, **kwargs):
        result = self.job_repository.find_by(**kwargs)
        if result is not None:
            return self.build_response(result)
        else:
            return None

    def create_job(self, job_request: JobRequest):
        row_id = self.job_repository.insert(**job_request.__dict__)
        return row_id
