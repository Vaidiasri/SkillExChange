from ..lib.database import Base
from sqlalchemy.dialects.postgresql import  UUID
import uuid
from sqlalchemy import  Column,String
from sqlalchemy.orm import  relationship
class Skill(Base):
  __tablename__="skills"
  id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
  skill=Column(String,nullable=False)
  # Magic Line: Ye batata hai ki Skill 'Junction' table se judi hai
  owners = relationship("Junction", back_populates="skill_link")