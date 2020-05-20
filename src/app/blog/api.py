from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.app.auth.logic import get_current_user, get_current_active_superuser
from src.app.base.utils.db import get_db

from src.app.user.models import User
from src.app.blog import schemas
from src.app.blog import service


blog_router = APIRouter()


@blog_router.post("/category", response_model=schemas.CategoryInDB)
def create_category(
        item: schemas.CategoryCreate,
        db: Session = Depends(get_db),
        current: User = Depends(get_current_active_superuser)
    ):
    """Create category"""
    return service.category.create(db_session=db, obj_in=item)


@blog_router.get("/category", response_model=List[schemas.CategoryInDB])
def get_list_category(db: Session = Depends(get_db)):
    """Get list category"""
    return service.category.get_multi(db_session=db)


@blog_router.get("/category/{pk}", response_model=schemas.CategoryInDB)
def get_category(pk: int, db: Session = Depends(get_db)):
    """Get single category"""
    query = service.category.get(db_session=db, id=pk)
    if not query:
        raise HTTPException(status_code=404, detail="Not found")
    return query


@blog_router.post("/tag", response_model=schemas.Tag)
def create_tag(
        item: schemas.TagCreateUpdate,
        db: Session = Depends(get_db),
        current: User = Depends(get_current_active_superuser)
    ):
    """Create tag"""
    return service.tag.create(db_session=db, obj_in=item)


@blog_router.get("/tag", response_model=List[schemas.Tag])
def get_list_tag(db: Session = Depends(get_db)):
    """Get list tag"""
    return service.tag.get_multi(db_session=db)


@blog_router.get("/tag/{pk}", response_model=schemas.Tag)
def get_tag(pk: int, db: Session = Depends(get_db)):
    """Get single tag"""
    query = service.tag.get(db_session=db, id=pk)
    if not query:
        raise HTTPException(status_code=404, detail="Not found")
    return query


@blog_router.post("/post", response_model=schemas.PostCreateUpdateInDB)
def create_post(
        item: schemas.PostCreateUpdate,
        db: Session = Depends(get_db),
        user: User = Depends(get_current_active_superuser)
    ):
    """Create post"""
    return service.post.create(db_session=db, obj_in=item, user=user)


@blog_router.get("/post", response_model=List[schemas.Post])
def get_list_post(db: Session = Depends(get_db)):
    """Get list post"""
    return service.post.get_multi(db_session=db)


@blog_router.get("/post/{pk}", response_model=schemas.Post)
def get_post(pk: int, db: Session = Depends(get_db)):
    """Get single post"""
    query = service.post.get(db_session=db, id=pk)
    if not query:
        raise HTTPException(status_code=404, detail="Not found")
    return query
