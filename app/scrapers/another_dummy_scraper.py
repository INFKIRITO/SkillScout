from typing import List
from app.scrapers.base import jobScraper
from app.schemas.job import Job


class AnotherDummyScraper(jobScraper):

    async def fetch_jobs(self, skills: List[str]) -> List[Job]:
        return [
            Job(
                title="FastAPI Backend Engineer",
                company="Sample Inc",
                location="India",
                url="https://example.com/job/2",
                source="dummy-2"
            )
        ]
