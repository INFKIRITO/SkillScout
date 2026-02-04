class SkillService:
    def __init__(self):
        self._skills = []

    def add_skills(self,skill: list[str]):
        self._skills.extend(skill)

    def get_all_skills(self):
        return self._skills