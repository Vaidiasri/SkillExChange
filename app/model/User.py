from ..lib.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import  relationship

class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String(100), nullable=True)

    email = Column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )
    # Magic Line: Ye batata hai ki User 'Junction' table se juda hai
    skills = relationship("Junction", back_populates="user_link")
