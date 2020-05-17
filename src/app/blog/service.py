from sqlalchemy.orm import Session
from src.app.base.crud_base import CRUDBase

from . import models
from . import schemas


class CRUDCategory(CRUDBase[schemas.CategoryInDB, schemas.CategoryCreateUpdate]):
    pass


class CRUDTag(CRUDBase[schemas.Tag, schemas.TagCreateUpdate]):
    pass


class CRUDPost(CRUDBase[schemas.Post, schemas.PostCreateUpdate]):
    pass


# class CRUDComments(CRUDBase[]):
#     pass
#
#
# class CRUDSearch(CRUDBase[]):
#     pass

