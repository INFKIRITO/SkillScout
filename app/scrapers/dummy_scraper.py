from typing import List
from app.schemas.job import Job
from app.scrapers.base import jobScraper


class DummyScraper(jobScraper):
    async def fetch_jobs(self, skills: List[str]) -> List[Job]:
        return [
            Job(
                title="Python Developer",
                company="Tech Corp",
                location="Pune, India",
                url="https://techcorp.com/jobs/123",
                source="DummyScraper"
            )
        ]