#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Anmenity,
            'Review': Review
    }

    def all(self):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            cls_obj = {}
            to _add = []
            for val in FileStorage.__objects.values():
                if val.to_dict()['__class__'] == cls.__name__:
                    to_add.append(val.to_dict()['__class__'] + '.' + val.id)
            for i in to_add:
                cls_obj[i] = FileStorage.__objects[i]
            return cls_obj
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update(
                {obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = FileStorage.classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an obj"""
        if obj:
            del self.all()[obj.to_dict()['__class__'] + '.' + obj.id]
            self.save()

    def close(self)
    """
    close function
    """
    self.reload
