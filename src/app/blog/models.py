from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, sql, Table
from sqlalchemy.orm import relationship, backref

from src.db.session import Base


class Category(Base):
    """Класс модели категорий сетей"""
    __tablename__ = 'blog_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    published = Column(Boolean, default=True)
    description = Column(String(300))
    parent_id = Column(Integer, ForeignKey('blog_categories.id', ondelete="SET NULL"), nullable=True)
    children = relationship("Category", backref=backref('parent', remote_side=[id]))


tags = Table(
    'tags',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('post_id', Integer, ForeignKey('blog_posts.id')),
    Column('tag_id', Integer, ForeignKey('blog_tags.id'))
)


class Tag(Base):
    """Класс модели тегов"""
    __tablename__ = 'blog_tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    # post = relationship("Post", secondary=tags, back_populates="tag")


class Post(Base):
    """Класс модели новости"""
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    category_id = Column(Integer, ForeignKey('blog_categories.id', ondelete="SET NULL"))
    title = Column(String(500))
    mini_text = Column(String(50000))
    text = Column(String)
    created_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    published_date = Column(DateTime, server_default=sql.func.now())
    image = Column(String, nullable=True)
    published = Column(Boolean, default=True)
    viewed = Column(Integer, default=0)
    description = Column(String(300))

    author = relationship("User")
    category = relationship("Category")
    # tag = relationship("Tag", secondary=tags, back_populates="post")
    tags = relationship("Tag", secondary=tags, backref=backref('posts', lazy="dynamic"))


class Comment(Base):
    """Модель коментариев к новостям"""
    __tablename__ = 'blog_comments'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    post = Column(Integer, ForeignKey("blog_posts.id", ondelete="CASCADE"))
    parent_id = Column(Integer, ForeignKey('blog_comments.id'), nullable=True)
    children = relationship('Comment', backref=backref('parent', remote_side=[id]), lazy='dynamic')
    message = Column(String(2000))
    created_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    update_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    published = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)


class SpySearch(Base):
    """Модель отслеживания запросов поиска"""
    __tablename__ = 'blog_search'
    id = Column(Integer, primary_key=True)
    record = Column(String(1000))
    counter = Column(Integer, default=0)
