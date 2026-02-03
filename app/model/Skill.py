from ..lib.database import Base
from sqlalchemy.dialects.postgresql import  UUID
import uuid
from sqlalchemy import  Column,String
class Skill(Base):
  __tablename__="skills"
  id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
  skill=Column(String,nullable=False)