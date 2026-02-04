class HealthService:
    def getstatus(self):
        return {
            "status": "healthy",
            "message": "The SkillScout AI service is operational."
        }