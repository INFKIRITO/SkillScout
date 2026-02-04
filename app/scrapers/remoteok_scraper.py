import httpx
from typing import List

from app.scrapers.base import jobScraper
from app.schemas.job import Job


class RemoteOKScraper(jobScraper):
    BASE_URL = "https://remoteok.com/api"

    async def fetch_jobs(self, skills: List[str]) -> List[Job]:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(self.BASE_URL)
            response.raise_for_status()

            data = response.json()

        jobs: List[Job] = []

        # First element is metadata → skip it
        for item in data[1:]:
            title = item.get("position")
            company = item.get("company")
            url = item.get("url")

            if not title or not company or not url:
                continue

            jobs.append(
                Job(
                    title=title,
                    company=company,
                    location=item.get("location"),
                    url=url,
                    source="remoteok"
                )
            )

        return jobs
