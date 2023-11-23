from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industry = []

        for job in self.jobs_list:
            type = job["industry"]
            if type not in unique_industry and type != '':
                unique_industry.append(type)

        print(unique_industry)
        return unique_industry


p = ProcessIndustries()
p.read()
print('ok')
