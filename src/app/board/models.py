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
    'teams',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('project_id', Integer, ForeignKey('board_projects.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)


class Project(Base):
    __tablename__ = 'board_projects'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(350))
    description = Column(String(50000))
    create_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    language_id = Column(Integer, ForeignKey("board_toolkit.id"))
    category_id = Column(Integer, ForeignKey("board_categories.id"))

    user = relationship("User", backref="projects")
    language = relationship("Toolkit", backref="projects")
    category = relationship("Category", backref="projects")
    team = relationship("User", secondary=team, backref=backref('projects', lazy="dynamic"))

    def __repr__(self):
        return f'<Project("{self.name}")'


class Task(Base):
    __tablename__ = 'board_tasks'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    description = Column(String(10000))
    create_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"))
    user = relationship("User", backref="u_tasks", foreign_keys=[user_id])

    worker_id = Column(Integer, ForeignKey('user.id', ondelete="SET NULL"), nullable=True)
    worker = relationship("User", backref="w_tasks", foreign_keys=[worker_id])

    project_id = Column(Integer, ForeignKey('board_projects.id', ondelete="CASCADE"))
    project = relationship("Project", backref="tasks")

    def __repr__(self):
        return f'<Task("{self.id}")'


class CommentTask(Base):
    __tablename__ = 'board_comments_task'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    message = Column(String(1000))
    create_date = Column(DateTime(timezone=True), server_default=sql.func.now())
    task_id = Column(Integer, ForeignKey('board_tasks.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"))

    task = relationship("Task", backref="comment_tasks")
    user = relationship("User", backref="comment_tasks")

    def __repr__(self):
        return f'<CommentTask("{self.task} - {self.user}")'
