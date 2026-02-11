from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Union

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Union[str, None] = None

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    class Config:
        from_attributes=True

class UserInDB(UserOut):
    hashed_password: str