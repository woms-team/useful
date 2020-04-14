from sqlalchemy import Column, String, Integer, DateTime, Boolean
from src.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String(150))
    last_name = Column(String(150))
    date_join = Column(DateTime)
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    avatar = Column(String)

