#!/usr/bin/python3
""""""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class contains unit tests for the BaseModel class.
    """

    def test_init(self):
        """
        Tests the initialization of a BaseModel instance.
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertTrue(isinstance(my_model.id, str))
        self.assertRegex(my_model.id, r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$')  
        self.assertIsInstance(my_model.created_at, datetime)  
        self.assertIsNone(my_model.updated_at)

    def test_save(self):
        """
        Tests the save method of a BaseModel instance.
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at 
        my_model.save()
        current_updated_at = my_model.updated_at  

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Tests the to_dict method of a BaseModel instance.
        """
        my_model = BaseModel()
        my_model.save()  

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        """
        Tests the string representation of a BaseModel instance.
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
