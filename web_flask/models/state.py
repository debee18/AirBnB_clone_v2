#!/usr/bin/python3
"""
State class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """
    State class for the State table
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """
            Returns the list of City objects from storage linked to the current State
            """
            cities_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

