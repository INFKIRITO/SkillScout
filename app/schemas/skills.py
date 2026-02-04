from pydantic import BaseModel, Field
from typing import List

class SkillRequest(BaseModel):
    skills: List[str] = Field(
        ...,
        example=["Python", "Machine Learning", "Data Analysis"],
        description="List of skills to be processed"
    )

class SkillResponse(BaseModel):
    message: str 
    total_skills: int 
        