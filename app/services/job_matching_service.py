from typing import List
from app.schemas.job import Job


class JobMatchingService:
    def score_jobs(self, jobs: List[Job], skills: List[str]) -> List[Job]:
        scored_jobs = []

        normalized_skills = [s.lower() for s in skills]

        for job in jobs:
            score = 0.0
            title = job.title.lower()

            for skill in normalized_skills:
                if skill in title:
                    score += 1.0

            job.score = score
            scored_jobs.append(job)

        scored_jobs.sort(key=lambda j: j.score or 0, reverse=True)
        return scored_jobs
