from abc import ABC, abstractmethod
from typing import List
from app.schemas.job import Job

class jobScraper(ABC):
    
    
    @abstractmethod
    async def fetch_jobs(self, skills: List[str]) -> List[Job]:
        pass