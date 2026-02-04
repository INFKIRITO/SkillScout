from pydantic import BaseModel, Field
from typing import Optional

class Job(BaseModel):
    title: str
    company: str
    location:Optional[str]
    url: str
    source: str
    score: Optional[float] = None