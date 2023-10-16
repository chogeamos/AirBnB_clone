#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Define a dictionary to map class names to their respective classes
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Serialize instances to a JSON file and deserialize back to instances."""

    # A string representing the path to the JSON file
    __file_path = "file.json"
    # A dictionary to store all objects by <class name>.id
    __objects = {}

    def get_all(self, target_class=None):
        """Return the dictionary __objects, optionally filtered by class."""
        if target_class is not None:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if target_class == value.__class__ or target_class == value.__class__.__name__:
                    filtered_dict[key] = value
            return filtered_dict
        return self.__objects

    def add(self, obj):
        """Store the object in __objects with the key <obj class name>.id."""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save_changes(self):
        """Serialize __objects to the JSON file specified by __file_path."""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict(save_check=True)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload_data(self):
        """Deserialize the JSON file into __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                json_data = json.load(f)
            for key in json_data:
                obj_data = json_data[key]
                obj_class = classes[obj_data["__class__"]]
                self.__objects[key] = obj_class(**obj_data)
        except:
            pass

    def get_object(self, target_class, obj_id):
        """Retrieve an object by class and/or id."""
        key = f"{target_class.__name__}.{obj_id}"

        if key in self.__objects:
            return self.__objects[key]
        else:
            return None

    def count_objects(self, target_class=None):
        """Return the count of objects in storage, optionally filtered by class."""
        return len(self.get_all(target_class))

    def remove(self, obj=None):
        """Remove an object from __objects if it exists."""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close_session(self):
        """Reload the data by deserializing the JSON file into objects."""
        self.reload_data()

