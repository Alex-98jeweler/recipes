from ast import For
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean


Base = declarative_base()

class Users(Base):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    nickname = Column('nickname', String(30), unique=True)
    password = Column('password', String)
    email = Column('email', String)
    status = Column('is_active', Boolean, default=True)


class Recipes(Base):
    __tablename__ = 'recipes'

    id = Column('id', Integer, primary_key=True)
    author_id = Column('author_id', Integer, ForeignKey('users.id'))
    create_date = Column('create_date', DateTime)
    title = Column('title', String)
    description = Column("description", String)
    type = Column("type", String)
    photo = Column("photo", String)
    likes = Column('likes', Integer, default=0)
    hashtags = Column('hashtags', String)
    status = Column('is_active', Boolean, default=True)


class Steps(Base):
    __tablename__ = 'steps'

    id = Column('id', Integer, primary_key=True)
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipes.id'))
    steps = Column('steps', String)


class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipes.id'))

