from sqlalchemy.orm import Session
from src.app.base.crud_base import CRUDBase

from src.app.user.models import User
from . import models
from . import schemas


class CRUDCategory(CRUDBase[models.Category, schemas.CategoryCreate, schemas.CategoryUpdate]):
    pass


class CRUDTag(CRUDBase[models.Tag, schemas.TagCreateUpdate, schemas.TagCreateUpdate]):
    pass


class CRUDPost(CRUDBase[models.Post, schemas.PostCreateUpdate, schemas.PostCreateUpdate]):

    def create(self, db_session: Session, *, obj_in: schemas.PostCreateUpdate, user: User) -> models.Post:
        db_obj = models.Post(
            title=obj_in.title,
            mini_text=obj_in.mini_text,
            text=obj_in.text,
            description=obj_in.description,
            category_id=obj_in.category_id,
            published_date=obj_in.published_date,
            #image=obj_in.image,
            published=obj_in.published,
            author_id=user.id
        )
        tags = db_session.query(models.Tag).filter(models.Tag.id.in_(obj_in.tags)).all()
        db_obj.tags = [tag for tag in tags]
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
tag = CRUDTag(models.Tag)
post = CRUDPost(models.Post)
