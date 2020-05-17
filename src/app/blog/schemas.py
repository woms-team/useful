from datetime import datetime
from typing import List

from pydantic import BaseModel
from src.app.user.schemas import User


class CategoryBase(BaseModel):
    """Base model category"""
    name: str
    published: bool
    description: str
    parent_id: int = None


class CategoryBaseInDB(BaseModel):
    """BaseInDB model category"""
    name: str

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    """Create category"""
    pass


class CategoryUpdate(CategoryBase):
    """Update category"""
    pass


class CategoryInDB(CategoryBase):
    """Single category"""
    id: int

    class Config:
        orm_mode = True


class CategoryChildren(CategoryInDB):
    """Category and children"""
    children: List[CategoryInDB]


class TagBase(BaseModel):
    """Tag base model"""
    name: str


class TagCreateUpdate(TagBase):
    """Tag create and update"""
    pass


class Tag(TagBase):
    """Tag in db"""
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    """Post base model"""
    title: str
    mini_text: str
    text: str
    description: str


class PostCreateUpdate(PostBase):
    """Post create and update"""
    category_id: int
    published_date: datetime
    image: bytes = None
    published: bool = True


class PostCreateUpdateInDB(PostCreateUpdate):
    """Post create and update"""
    id: int
    author_id: int


class Post(PostBase):
    id: int
    created_date: datetime
    published_date: datetime
    viewed: int
    author: User
    category: CategoryBaseInDB

    class Config:
        orm_mode = True
