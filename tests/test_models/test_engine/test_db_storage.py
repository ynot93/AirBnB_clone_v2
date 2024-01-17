#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import unittest
from models import storage
from models.user import User
from datetime import datetime
import os
import MySQLdb


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db_storage test not supported')
class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """ Set up test environment """
        storage.reload()

    def tearDown(self):
        """ Tear down test environment """
        storage.close()

    def test_new_and_save(self):
        """ Test that new and save methods work correctly """
        new_user = User(first_name='john', last_name='doe', email='john@example.com', password='password')
        storage.new(new_user)
        storage.save()

        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchone()
        db.close()

        self.assertEqual(new_count[0], 1)

    def test_new(self):
        """ Test that a new object is correctly added to the database """
        new_user = User(first_name='john', last_name='doe', email='john@example.com', password='password')
        storage.new(new_user)
        storage.save()

        self.assertIn(new_user, storage.all(User).values())

    def test_delete(self):
        """ Test that an object is correctly deleted from the database """
        new_user = User(first_name='john', last_name='doe', email='john@example.com', password='password')
        storage.new(new_user)
        storage.save()

        self.assertTrue(new_user in storage.all(User).values())

        storage.delete(new_user)
        self.assertNotIn(new_user, storage.all(User).values())

    def test_reload(self):
        """ Test the reloading of the database session """
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cur = db.cursor()
        cur.execute('INSERT INTO users(id, created_at, updated_at, email, password, first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
                    ['4447-by-me', str(datetime.now()), str(datetime.now()), 'john@example.com', 'pass', 'John', 'Doe'])
        db.commit()
        db.close()

        self.assertIn('User.4447-by-me', storage.all())

    def test_save(self):
        """ Test that an object is successfully saved to the database """
        new_user = User(first_name='john', last_name='doe', email='john@example.com', password='password')
        storage.new(new_user)
        storage.save()

        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cur = db.cursor()
        cur.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cur.fetchone()
        cur.execute('SELECT COUNT(*) FROM users;')
        new_count = cur.fetchone()[0]
        db.close()

        self.assertFalse(result is None)
        self.assertEqual(new_count, 1)
        self.assertTrue(new_user in storage.all().values())

if __name__ == '__main__':
    unittest.main()
