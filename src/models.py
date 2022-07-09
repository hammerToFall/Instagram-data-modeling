import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Publish(Base):
    __tablename__ = 'publish'
    id = Column(Integer, primary_key=True)
    post = Column(String(250), ForeignKey('user.id'))
    story = Column(String(250))
    reel = Column(String(250), nullable=False)
   # person = relationship(Person)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), ForeignKey('publish.post'))
    autor_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, nullable=False)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    likes_num = Column(Integer, ForeignKey('publish.reel'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')