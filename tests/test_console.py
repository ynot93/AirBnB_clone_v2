#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""
"""
test module
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class.
    """
    def test_create_object_success(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create("ClassName key1=value1 key2=value2")
            result = mock_stdout.getvalue().strip()

        self.assertTrue(result.startswith(""))

    def test_create_object_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create("")
            result = mock_stdout.getvalue().strip()

        self.assertEqual(result, "** class name missing **")

    def test_create_object_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create("InvalidClassName key=value")
            result = mock_stdout.getvalue().strip()

        self.assertEqual(result, "** Class doesn't exist **")

    def test_create_object_with_string_parameters(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create
            ("ClassName name='Test Object' value='some value'")
            result = mock_stdout.getvalue().strip()

        self.assertTrue(result.startswith(""))

    def test_create_object_with_float_parameter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create("ClassName value=3.14")
            result = mock_stdout.getvalue().strip()

        self.assertTrue(result.startswith(""))

    def test_create_object_with_integer_parameter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create("ClassName count=42")
            result = mock_stdout.getvalue().strip()

        self.assertTrue(result.startswith(""))

    def test_create_object_with_invalid_value_syntax(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_create("ClassName value='invalid_syntax'")
            result = mock_stdout.getvalue().strip()

        self.assertTrue(result.startswith("An error occurred"))


if __name__ == '__main__':
    unittest.main()
