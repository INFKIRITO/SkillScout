from app.services.health_service import HealthService
from app.services.skill_service import SkillService
from app.services.job_scraper_service import JobScraperService
from app.services.job_matching_service import JobMatchingService

# 🔥 SINGLETON INSTANCES (created once at import time)
_skill_service = SkillService()
_job_scraper_service = JobScraperService()
_job_matcher_service = JobMatchingService()


def get_health_service() -> HealthService:
    return HealthService()  # stateless, OK


def get_skill_service() -> SkillService:
    return _skill_service   # ✅ SAME instance every time


def get_job_scraper_service() -> JobScraperService:
    return _job_scraper_service  # ✅ SAME instance

def get_job_matching_service() -> JobMatchingService:
    return _job_matcher_service  # ✅ SAME instance

