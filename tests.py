#!flask/bin/python
import os
import unittest

from app import app, db, user_datastore
import config


class TestCase(unittest.TestCase):
    def setUp(self):
        print("Setting up test environment")

        configuration = config.TestConfig()
        app.config.from_object(configuration)

        self.app = app.test_client()

        db.create_all()
        user_datastore.create_user(email='troman360@gmail.com', password='password')
        db.session.commit()

    def test_login_logout(self):
        print("Testing login")

        response = self.login('troman360@gmail.com', 'password')
        assert "200" in response.status

        print("Testing logout")

        response = self.logout()
        assert "200" in response.status

    def tearDown(self):
        print("Tearing down test environment")

        db.session.remove()
        db.drop_all()
        os.environ['ENV'] = 'DEV'

    def login(self, email, password):
        return self.app.post('/login', data=dict(email=email, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
