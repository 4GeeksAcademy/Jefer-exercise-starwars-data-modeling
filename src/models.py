import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), nullable=False)
    email = Column(String(32),nullable=False)
    password = Column(String(16), nullable=False)
    created_account_date = Column(String)
    profile_picture = Column(String)



class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    FavoriteID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('User.UserID'))
    user = relationship(User)

class Vehicles(Base):
    __tablename__ = 'Vehicles'

    VechilesID = Column(Integer, primary_key=True)
    FavoritesID = Column(Integer, ForeignKey('Favorites.FavoritesID'))
    favorites = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'Planets'

    PlanetsID = Column(Integer, primary_key=(True))
    FavoritesID = Column(Integer, ForeignKey('Favorites.FavoritesID'))
    favorites = relationship(Favorites)

class Peoples(Base):
    __tablename__ = 'Peoples'

    PeoplesID = Column(Integer, primary_key=(True))
    FavoritesID = Column(Integer, ForeignKey('Favorites.FavoritesID'))
    favorites = relationship(Favorites)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
