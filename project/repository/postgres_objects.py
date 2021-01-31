from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)

    username = Column(String(128))
    password = Column(String(128))
    email = Column(String(128))
    createdAt = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updatedAt = Column(DateTime, onupdate=datetime.datetime.utcnow)


class Parent(Base):
    __tablename__ = 'parent'

    parent_id = Column(Integer, primary_key=True)

    name = Column(String(128))
    child = relationship("Child", back_populates="parent")
    createdAt = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updatedAt = Column(DateTime, onupdate=datetime.datetime.utcnow)


class Child(Base):
    __tablename__ = 'child'

    child_id = Column(Integer, primary_key=True)

    name = Column(String(128))
    parent_id = Column(Integer, ForeignKey('parent.parent_id'))
    parent = relationship("Parent", back_populates="child")
    createdAt = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updatedAt = Column(DateTime, onupdate=datetime.datetime.utcnow)
