#!/usr/bin/python3
"""Amenity test """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest


class TestAmenity(test_basemodel):
    """Amenity test class"""

    def __init__(self, *args, **kwargs):
        """Init the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Testing name type"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        amenity = self.value()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test that Amenity has the expected attributes"""
        amenity = self.value()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attributes_type(self):
        """Test that Amenity attributes have the correct types"""
        amenity = self.value()
        self.assertIsInstance(amenity.name, str)

    def test_attributes_default_value(self):
        """Test that Amenity attributes have the correct default values"""
        amenity = self.value()
        self.assertEqual(amenity.name, "")

@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'not testing file storage')
class TestAmenityFileStorage(unittest.TestCase):
    def test_relationship(self):
        """Test that Amenity has the correct relationship with Place in file storage"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'place_amenities'))
        self.assertIsInstance(amenity.place_amenities, list)

if __name__ == '__main__':
    unittest.main()
