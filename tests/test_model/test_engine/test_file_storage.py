#!/usr/bin/python3
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """
    TestFileStorage_instantiation class contains unit tests for FileStorage instantiation.
    """

    def test_FileStorage_instantiation_no_args(self):
        """
        Test FileStorage instantiation with no arguments.
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """
        Test FileStorage instantiation with an argument.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """
        Test if the file_path attribute is a private string.
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """
        Test if the __objects attribute is a private dictionary.
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """
        Test if models.storage initializes a FileStorage instance.
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    TestFileStorage_methods class contains unit tests for FileStorage methods.
    """

    def setUp(self):
        """
        Set up method to prepare for each test case.
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down method to clean up after each test case.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        Test if all() method returns a dictionary.
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """
        Test all() method with an argument.
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """
        Test the new() method.
        """
        my_base_model = BaseModel()
        models.storage.new(my_base_model)
        self.assertIn("BaseModel." + my_base_model.id, models.storage.all().keys())
        self.assertIn(my_base_model, models.storage.all().values())

    def test_new_with_args(self):
        """
        Test new() method with arguments.
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """
        Test new() method with None.
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """
        Test the save() method.
        """
        my_base_model = BaseModel()
        models.storage.new(my_base_model)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_base_model.id, save_text)

    def test_save_with_arg(self):
        """
        Test save() method with an argument.
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """
        Test the reload() method.
        """
        my_base_model = BaseModel()
        models.storage.new(my_base_model)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + my_base_model.id, objs)

    def test_reload_with_arg(self):
        """
        Test reload() method with an argument.
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
