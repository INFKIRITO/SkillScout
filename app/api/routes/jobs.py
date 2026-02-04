import logging
from fastapi import APIRouter, Query, Depends
from typing import List
from app.schemas.job import Job
from app.services.job_matching_service import JobMatchingService
from app.services.skill_service import SkillService
from app.services.job_scraper_service import JobScraperService
from app.api.dependencies import get_skill_service
from app.api.dependencies import get_job_scraper_service
from app.api.dependencies import get_job_matching_service
from fastapi import Query
from app.schemas.pagination import PaginatedResponse


router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["Jobs"]
)

logger = logging.getLogger(__name__)


@router.get("/", response_model=PaginatedResponse[Job])
async def get_jobs(
    limit: int = Query(10, ge=1, le=50),
    offset: int = Query(0, ge=0),
    skill_service: SkillService = Depends(get_skill_service),
    scraper_service: JobScraperService = Depends(get_job_scraper_service),
    matcher: JobMatchingService = Depends(get_job_matching_service)
):
    logger.info("Fetching paginated jobs")

    skills = skill_service.get_all_skills()
    if not skills:
        return PaginatedResponse(
            total=0,
            limit=limit,
            offset=offset,
            items=[]
        )

    jobs = await scraper_service.fetch_all_jobs(skills)
    matched_jobs = matcher.score_jobs(jobs, skills)

    total = len(matched_jobs)
    paginated_items = matched_jobs[offset : offset + limit]

    return PaginatedResponse(
        total=total,
        limit=limit,
        offset=offset,
        items=paginated_items
    )

