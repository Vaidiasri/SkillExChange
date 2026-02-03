from ..lib.database import Base
from sqlalchemy import Column,ForeignKey,String
from sqlalchemy.orm import relationship
import  uuid
from sqlalchemy.dialects.postgresql import  UUID
class Junction(Base):
  __tablename__="user_skill"
  id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
  user_id=Column(UUID(as_uuid=True),ForeignKey("users.id"),nullable=False)
  skill_id=Column(UUID(as_uuid=True),ForeignKey("skills.id"),nullable=False)
  # Proficiency add kar sakte hain (Optional par accha hai)
  proficiency = Column(String, default="Beginner") 

    # Magic Lines: Upar wale tables se wapas baat karne ke liye
  user_link = relationship("User", back_populates="skills")
  skill_link = relationship("Skill", back_populates="owners")

