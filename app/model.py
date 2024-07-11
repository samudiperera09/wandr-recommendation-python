from sqlalchemy import Column, String, Integer, JSON, TIMESTAMP, ForeignKey, text, select
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from config import Base


class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)


class Activities(Base):
    __tablename__ = 'activities'
    activity_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

class Traveller(Base):
    __tablename__ = 'travellers'
    traveller_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    country = Column(String(255), nullable=False)
    categories = Column(JSON, nullable=False)
    activities = Column(JSON, nullable=False)
    profile_image = Column(String(255), nullable=True)
    jwt = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    membership = Column(String(255), nullable=False)

    @hybrid_property
    def category_ids(self):
        return self.categories

    @hybrid_property
    def activity_ids(self):
        return self.activities
    

