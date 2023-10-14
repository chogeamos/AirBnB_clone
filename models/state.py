#!/usr/bin/python3
"""Defines the State class."""

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Represents a State."""
    
    # Use the 'q' variable to check the storage type
    q = models.storage_t
    
    if q == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a State."""
        super().__init__(*args, **kwargs)

    if q != "db":
        @property
        def cities(self):
            """Getter for a list of City instances related to the state."""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

