from typing import List, Dict
from app.schemas.job import Job


class JobDeduplicationService:
    def deduplicate(self, jobs: List[Job]) -> List[Job]:
        unique_jobs: Dict[str, Job] = {}

        for job in jobs:
            key = self._make_key(job)

            # If job already exists, keep the one with higher score
            if key in unique_jobs:
                existing = unique_jobs[key]
                if (job.score or 0) > (existing.score or 0):
                    unique_jobs[key] = job
            else:
                unique_jobs[key] = job

        return list(unique_jobs.values())

    def _make_key(self, job: Job) -> str:
        title = job.title.lower().strip()
        company = job.company.lower().strip()
        location = (job.location or "").lower().strip()

        return f"{title}|{company}|{location}"
