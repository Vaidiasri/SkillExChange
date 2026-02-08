from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..model import Skill as SkillModel
from ..schema.skill import Skill, SkillOut
from ..lib.database import get_db
from uuid import UUID

router = APIRouter(prefix="/skills", tags=["Skills"])

# Create skill
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SkillOut)
async def create_skill(request: Skill, db: AsyncSession = Depends(get_db)):
    new_skill = SkillModel(
        name=request.name,
        description=request.description,
        level=request.level
    )
    db.add(new_skill)
    await db.commit()
    await db.refresh(new_skill)
    return new_skill

# Get all skills
@router.get("/", response_model=list[SkillOut])
async def get_all_skills(db: AsyncSession = Depends(get_db)):
    stmt = select(SkillModel)
    result = await db.execute(stmt)
    skills = result.scalars().all()
    return skills

# Get skill by ID
@router.get("/{skill_id}", response_model=SkillOut)
async def get_skill(skill_id: UUID, db: AsyncSession = Depends(get_db)):
    stmt = select(SkillModel).where(SkillModel.id == skill_id)
    result = await db.execute(stmt)
    skill = result.scalars().first()
    
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")
    return skill

# Delete skill
@router.delete("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill(skill_id: UUID, db: AsyncSession = Depends(get_db)):
    stmt = select(SkillModel).where(SkillModel.id == skill_id)
    result = await db.execute(stmt)
    skill = result.scalars().first()
    
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")
    
    await db.delete(skill)
    await db.commit()