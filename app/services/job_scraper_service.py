import asyncio
import logging
from typing import List

from app.schemas.job import Job
from app.scrapers.dummy_scraper import DummyScraper
from app.scrapers.another_dummy_scraper import AnotherDummyScraper
from app.core.cache import InMemoryCache
from app.scrapers.remoteok_scraper import RemoteOKScraper


logger = logging.getLogger(__name__)


class JobScraperService:
    def __init__(self):
        self.scrapers = [
            RemoteOKScraper(),
            DummyScraper(),
            AnotherDummyScraper()
        ]
        self.cache = InMemoryCache(ttl_seconds=300)

    async def fetch_all_jobs(self, skills: List[str]) -> List[Job]:
        cache_key = ",".join(sorted(skills))

        cached_jobs = self.cache.get(cache_key)
        if cached_jobs is not None:
            logger.info("Returning cached jobs")
            return cached_jobs

        tasks = [
            self._safe_fetch(scraper, skills)
            for scraper in self.scrapers
        ]

        results = await asyncio.gather(*tasks)

        jobs: List[Job] = []
        for result in results:
            jobs.extend(result)

        self.cache.set(cache_key, jobs)
        return jobs
class JobScraperService:
    def __init__(self):
        self.scrapers = [
            RemoteOKScraper(),
            DummyScraper(),
            AnotherDummyScraper()
        ]

    async def _safe_fetch(self, scraper, skills: List[str], timeout: int = 5):
        try:
            return await asyncio.wait_for(
                scraper.fetch_jobs(skills),
                timeout=timeout
            )
        except asyncio.TimeoutError:
            logger.warning(f"{scraper.__class__.__name__} timed out")
            return []
        except Exception as e:
            logger.error(f"{scraper.__class__.__name__} failed: {e}")
            return []

    async def fetch_all_jobs(self, skills: List[str]) -> List[Job]:
        tasks = [
            self._safe_fetch(scraper, skills)
            for scraper in self.scrapers
        ]

        results = await asyncio.gather(*tasks)

        jobs: List[Job] = []
        for result in results:
            jobs.extend(result)

        return jobs