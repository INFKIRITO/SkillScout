import logging
from fastapi import APIRouter, Query
# from app.core.exceptions import InvalidInput
from app.schemas.health import HealthResponse

router = APIRouter(
    prefix="/api/v1",
    tags=["Health"]
)
logger = logging.getLogger(__name__)

@router.get("/health", response_model=HealthResponse)
def health_check():
    # if trigger_error:
    #     raise InvalidInput("Simulated exception for testing purpose")
    
    logger.info("Health check called")
    return HealthResponse(
        status="healthy",
        message="The SkillScout AI service is operational."
    )


