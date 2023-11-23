from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path="data/jobs.csv") -> List[Dict]:
        file = open(path, "r")
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        header, *data = content
        self.jobs_list = [header, *data]

    def get_unique_job_types(self) -> List[str]:
        unique_type = []

        for job in self.jobs_list:
            type = job["job_type"]
            if type not in unique_type:
                unique_type.append(type)
        return unique_type

    def filter_by_multiple_criteria(self, job_list, filter) -> List[dict]:
        if not isinstance(filter, dict):
            raise TypeError
        industry = filter["industry"]
        job_type = filter["job_type"]

        return [job for job in job_list
                if job['job_type'] == job_type
                and job["industry"] == industry]
