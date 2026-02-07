import logging
from fastapi import APIRouter, Query, Depends
from typing import List
from app.schemas import skills
from app.schemas.job import Job
from app.services.job_matching_service import JobMatchingService
from app.services.skill_service import SkillService
from app.services.job_scraper_service import JobScraperService
from app.services.job_deduplication_service import JobDeduplicationService
from app.api.dependencies import get_skill_service
from app.api.dependencies import get_job_scraper_service
from app.api.dependencies import get_job_matching_service
from fastapi import Query
from app.schemas.pagination import PaginatedResponse
from app.api.dependencies import get_job_deduplication_service
from app.services.semantic_matching_service import SemanticMatchingService
from app.core.config import settings



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
    matcher: JobMatchingService = Depends(get_job_matching_service),
    deduper: JobDeduplicationService = Depends(get_job_deduplication_service)

):
    logger.info("Fetching, matching, and deduplicating jobs")

    skills = skill_service.get_all_skills()
    if not skills:
        return PaginatedResponse(
            total=0, limit=limit, offset=offset, items=[]
        )

    jobs = await scraper_service.fetch_all_jobs(skills)
    logger.warning(f"AI MATCHING MODE = {settings.ai_matching_mode}")
    if settings.ai_matching_mode == "semantic":
        logger.warning("🔥 USING SEMANTIC MATCHING")
        semantic_matcher = SemanticMatchingService()
        matched_jobs = semantic_matcher.score_jobs(jobs, skills)
    else:
        logger.warning("⚠️ USING KEYWORD MATCHING")
        matched_jobs = matcher.score_jobs(jobs, skills)
    
    unique_jobs = deduper.deduplicate(matched_jobs)
    total = len(unique_jobs)
    paginated_items = unique_jobs[offset : offset + limit]

    return PaginatedResponse(
        total=total,
        limit=limit,
        offset=offset,
        items=paginated_items
    )


