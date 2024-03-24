#!/usr/bin/python3
"""Module defining the State class and creating Base instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    """Class representing a state

        Attributes:
            __tablename__ (str): The table name of the class
            id (int): The State id of the class
            name (str): The State name of the class"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
