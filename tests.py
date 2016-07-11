#!flask/bin/python
import os
import unittest

from app import app, db


class TestCase(unittest.TestCase):
    def setUp(self):
        os.environ['ENV'] = 'TEST'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
