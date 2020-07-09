from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str = None
    id: int = None


class Subcategory(CategoryBase):
    parent_id: int = None

