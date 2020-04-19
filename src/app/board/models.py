from sqlalchemy import Column, String, Integer, ForeignKey
from src.db.session import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(150))
    parent_id = Column(Integer, ForeignKey('category.id'))

    parent = relationship('Category', remote_side=id, backref='subcategories')

    def __repr__(self):
        return '<Category("{}")'.format(self.name)
