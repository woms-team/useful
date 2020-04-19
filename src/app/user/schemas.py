from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    first_name: Optional[str] = None


class UserBaseInDB(UserBase):
    id: int = None

    class Config:
        orm_mode = True


class UserCreate(UserBaseInDB):
    """ Properties to receive via API on creation
    """
    email: str
    password: str


class UserUpdate(UserBaseInDB):
    """ Properties to receive via API on update
    """
    password: Optional[str] = None


class User(UserBaseInDB):
    """ Additional properties to return via API
    """
    pass


class UserInDB(UserBaseInDB):
    """ Additional properties stored in DB
    """
    password: str
