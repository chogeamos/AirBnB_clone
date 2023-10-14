#!/usr/bin/python
"""Define the Amenity class."""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represent an Amenity."""
    
    # Use the 'q' variable to check the storage type
    q = models.storage_t
    
    if q == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize an Amenity."""
        super().__init__(*args, **kwargs)

