import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import SkillScoutException

logger = logging.getLogger(__name__)

def SkillScout_exception_handler(request: Request, exc: SkillScoutException):
    logger.error(f"handled SkillScoutException: {exc}")
    return JSONResponse(
        status_code=400,
        content={
            "error": exc.__class__.__name__,
            "message": str(exc)}
    )