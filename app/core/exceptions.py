class SkillScoutException(Exception):
    """Base exception for SkillScout AI"""
    pass


class ResourceNotFound(SkillScoutException):
    pass


class InvalidInput(SkillScoutException):
    pass
