#!/usr/bin/python
"""Defines the Review class."""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Represents a Review."""
    
    # Use the 'q' variable to check the storage type
    q = models.storage_t
    
    if q == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Review."""
        super().__init__(*args, **kwargs)

