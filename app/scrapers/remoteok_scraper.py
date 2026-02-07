import httpx
from typing import List

from app.scrapers.base import jobScraper
from app.schemas.job import Job


class RemoteOKScraper(jobScraper):
    BASE_URL = "https://remoteok.com/api"

    async def fetch_jobs(self, skills: List[str]) -> List[Job]:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
        }

        async with httpx.AsyncClient(timeout=10, headers=headers) as client:
            response = await client.get(self.BASE_URL)
            response.raise_for_status()
            data = response.json()

        jobs: List[Job] = []

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
