import logging
from fastapi import APIRouter, Query, Depends
from app.schemas.skills import SkillResponse, SkillRequest
from app.services.skill_service import SkillService
from app.api.dependencies import get_skill_service

router = APIRouter(
    prefix="/api/v1/skills",
    tags=["Skills"]
)

logger = logging.getLogger(__name__)

@router.post("/", response_model=SkillResponse)
def add_skills(
    payload: SkillRequest,
    service: SkillService = Depends(get_skill_service)
):
    logger.info("Adding user skills")
    service.add_skills(payload.skills)

    return SkillResponse(
        message="Skills added successfully",
        total_skills=len(service.get_all_skills())
    )