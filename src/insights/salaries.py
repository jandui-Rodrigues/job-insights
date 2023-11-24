from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        # min_salary
        max_salary = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"].isdigit()
        ]
        return max(max_salary)

    def get_min_salary(self) -> int:
        # min_salary
        min_salary = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"].isdigit()
        ]
        return min(min_salary)

    def validate_job(self, min_salary, max_salary):
        if min_salary == "" or max_salary == "":
            raise ValueError()
        if max_salary < min_salary:
            raise ValueError()

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            self.validate_job(min_salary, max_salary)
            if int(salary) <= max_salary and int(salary) >= min_salary:
                return True
            else:
                return False
        except (TypeError, ValueError, KeyError):
            raise ValueError

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        valid_jobs = []
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    valid_jobs.append(job)
            except ValueError:
                continue
        return valid_jobs
