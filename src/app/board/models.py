from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql, Table
from src.db.session import Base
from sqlalchemy.orm import relationship, backref


class Category(Base):
    __tablename__ = 'board_categories'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(150))
    parent_id = Column(
        Integer,
        ForeignKey('board_categories.id', ondelete="SET NULL"),
        nullable=True
    )
    children = relationship("Category", backref=backref('parent', remote_side=[id]))

    def __repr__(self):
        return f'<Category("{self.name}")'


class Toolkit(Base):
    __tablename__ = 'board_toolkit'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(150))
    parent_id = Column(
        Integer,
        ForeignKey('board_toolkit.id', ondelete="SET NULL"),
        nullable=True
    )
    children = relationship("Toolkit", backref=backref('parent', remote_side=[id]))

    def __repr__(self):
        return f'<Toolkit("{self.name}")'


team = Table(

)


class Project(Base):
    __tablename__ = 'board_projects'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(350))
    description = Column(String(50000))
    create_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    user = Column("User", ForeignKey("user.id"))
    language = Column("Toolkit", ForeignKey("board_toolkit.id"))
    category = Column("Category", ForeignKey("board_categories.id"))

    # team = M2M, User model

    def __repr__(self):
        return f'<Project("{self.name}")'


class Task(Base):
    __tablename__ = 'board_tasks'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    description = Column(String(10000))
    create_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    worker = Column("User", ForeignKey('user.id'))
    project = Column("Project", ForeignKey('board_projects.id'))

    def __repr__(self):
        return f'<Task("{self.id}")'


class CommentTask(Base):
    __tablename__ = 'board_comments_task'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    message = Column(String(1000))
    create_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    task = Column("task", ForeignKey('board_tasks.id'))
    user = Column("User", ForeignKey('user.id'))

    def __repr__(self):
        return f'<CommentTask("{self.task} - {self.user}")'
