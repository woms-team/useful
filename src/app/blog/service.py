from sqlalchemy.orm import Session
from src.app.base.crud_base import CRUDBase

from src.app.user.models import User
from . import models
from . import schemas


class CRUDCategory(CRUDBase[models.Category, schemas.CategoryCreate, schemas.CategoryUpdate]):
    pass


class CRUDTag(CRUDBase[models.Tag, schemas.TagCreateUpdate, schemas.TagCreateUpdate]):
    pass


class CRUDPost(CRUDBase[models.Post, schemas.Post, schemas.PostCreateUpdate]):

    def create(self, db_session: Session, user, obj_in: schemas.PostCreateUpdate) -> models.Post:
        db_obj = models.Post(**obj_in.dict(), author_id=user.id)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj


# class CRUDComments(CRUDBase[]):
#     pass
#
#
# class CRUDSearch(CRUDBase[]):
#     pass


category = CRUDCategory(models.Category)
tag = CRUDCategory(models.Tag)
post = CRUDCategory(models.Post)
