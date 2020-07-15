from typing import Optional
from sqlalchemy.orm import Session

from src.app.base.crud_base import CRUDBase
from .models import Category
from .schemas import CategoryBase, Subcategory


class CRUDCategory(CRUDBase[Category, Subcategory, CategoryBase]):
    """ CRUD for category """
    def get_category(self, db_session: Session, *, name: str) -> Optional[Category]:
        return db_session.query(Category).filter(Category.id == self.id).name

    def get_subcategory(self, db_session: Session, *, name: str) -> Optional[Category]:
        return db_session.query(Category).filter(Category.id == self.id).name



