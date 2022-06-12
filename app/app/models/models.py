from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from .meta import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    ext_id = Column(Text, unique=True)


class Scene(Base):
    __tablename__ = 'scenes'

    id = Column(Integer, primary_key=True)
    ext_id = Column(Text, unique=True)


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    address = Column(Text)
    ext_id = Column(Text, unique=True)


class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ext_id = Column(Text, unique=True)


class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    guid = Column(Text, unique=True)
    data = Column(JSONB)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    visit_id = Column(Integer, ForeignKey('visits.id'), nullable=False)
    scene_id = Column(Integer, ForeignKey('scenes.id'), nullable=False)
    camera = Column(Text)
