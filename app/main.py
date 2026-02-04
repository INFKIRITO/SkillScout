from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.core.config import settings
from app.core.logger import setup_logging
from app.core.exceptions import SkillScoutException
from app.core.error_handlers import SkillScout_exception_handler
from app.api.routes.skills import router as skills_router
from app.api.routes.jobs import router as jobs_router


def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(
    title = settings.app_name,
    version = "0.1.0"
)
    app.include_router(health_router)
    app.add_exception_handler(
        SkillScoutException,
        SkillScout_exception_handler
    )
    # inside create_app()
    app.include_router(skills_router)
    app.include_router(jobs_router)
    return app

app = create_app()

