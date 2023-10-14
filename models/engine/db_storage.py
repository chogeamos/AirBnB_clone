#!/usr/bin/python3
"""
This module contains the DBStorage class.
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Define a dictionary to map class names to their respective classes
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """Interacts with a MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a DBStorage object."""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def fetch_all(self, target_class=None):
        """Query the current database session."""
        results = {}
        for class_name, class_type in classes.items():
            if target_class is None or target_class is class_type or target_class is class_name:
                objects = self.__session.query(class_type).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    results[key] = obj
        return results

    def store_new(self, obj):
        """Add an object to the current database session."""
        self.__session.add(obj)

    def commit_changes(self):
        """Commit all changes in the current database session."""
        self.__session.commit()

    def remove_object(self, obj=None):
        """Remove an object from the current database session if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def refresh_data(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def retrieve_object(self, target_class, obj_id):
        """Retrieve an object by class and id."""
        if target_class in classes.values():
            return self.__session.query(target_class).filter(target_class.id == obj_id).first()
        else:
            return None

    def count_objects(self, target_class=None):
        """Count the number of objects in the storage."""
        return len(self.fetch_all(target_class))

    def close_session(self):
        """Call the remove() method on the private session attribute."""
        self.__session.remove()

