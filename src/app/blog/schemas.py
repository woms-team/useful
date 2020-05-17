from datetime import datetime
from typing import List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    """Base model category"""
    name: str
    published: bool
    description: str
    parent_id: int


class CategoryCreateUpdate(CategoryBase):
    """Create and update category"""
    pass


class CategoryInDB(CategoryBase):
    """Single category"""
    int: int

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
    author_id: int
    category_id: int
    published_date: datetime
    image: bytes = None
    published: bool = True


class Post(PostCreateUpdate):
    id: int
    created_date: datetime
    published_date: datetime
    viewed: int

    class Config:
        orm_mode = True
