#!/usr/bin/python3
import json
import os

from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class handles serialization and deserialization of instances
    to and from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file storing the serialized objects.
        __objects (dict): Dictionary to store objects in memory.
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns a dictionary of all objects stored in memory.

        Returns:
            dict: Dictionary containing all objects.
        """
        return FileStorage.__objects
    
    def save(self):
        """
        Saves objects from memory to the JSON file.
        """
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Reloads objects from the JSON file into memory.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
