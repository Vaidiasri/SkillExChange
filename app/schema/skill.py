from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None
    level: Optional[str] = None  # e.g., "beginner", "intermediate", "advanced"

class Skill(SkillBase):
    pass

class SkillOut(SkillBase):
    id: UUID
    
    class Config:
        from_attributes = True  