from app.services.health_service import HealthService
from app.services.skill_service import SkillService
from app.services.job_scraper_service import JobScraperService
from app.services.job_matching_service import JobMatchingService
from app.services.job_deduplication_service import JobDeduplicationService
from app.services.semantic_matching_service import SemanticMatchingService

# 🔥 SINGLETON INSTANCES (created once at import time)
_skill_service = SkillService()
_job_scraper_service = JobScraperService()
_job_matcher_service = JobMatchingService()
_job_duplication_service = JobDeduplicationService()
_jobsemantic_matcher_service = SemanticMatchingService()


def get_health_service() -> HealthService:
    return HealthService()  # stateless, OK


def get_skill_service() -> SkillService:
    return _skill_service   # ✅ SAME instance every time


def get_job_scraper_service() -> JobScraperService:
    return _job_scraper_service  # ✅ SAME instance

def get_job_matching_service() -> JobMatchingService:
    return _job_matcher_service  # ✅ SAME instance

def get_job_deduplication_service() -> JobDeduplicationService:
    return _job_duplication_service  # ✅ SAME instance

def get_semantic_matching_service() -> SemanticMatchingService:
    return _jobsemantic_matcher_service  # ✅ SAME instance
