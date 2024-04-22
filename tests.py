import json
import unittest
from fastapi.testclient import TestClient
from routes import app
from models import Session, User


class TestUserManagement(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.client = TestClient(app)

    def test_add_user(self):
        """
        Adding user test
        """
        response = self.client.post('/api/users', json={"username": "testClient", "email": "testEmail"})
        self.assertEqual(response.status_code, 200)  # Ожидаемый успешный статус создания пользователя

        # Проверка, что пользователь добавлен в базу данных
        user = self.session.query(User).filter_by(username="testClient").first()
        self.assertIsNotNone(user)

    def test_get_all_users(self):
        """
        Get all users test
        """
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        """
        Test to get current user
        """
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code, 200)

    def test_update_user_by_username(self):
        """
        Test to update username
        """
        response = self.client.put('/api/users/1', json={"username": "qwe", "email": None})
        self.assertEqual(response.status_code, 200)

    def test_update_user_by_email(self):
        """
        Test to update email
        """
        response = self.client.put('/api/users/1', json={"username": None, "email": "testUser_updated@gmail.com"})
        self.assertEqual(response.status_code, 200)


class TestDelete(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.client = TestClient(app)

    def test_delete_user(self):
        """
        Test delete user
        """
        response = self.client.delete('/api/users/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_user_fail(self):
        """
        Test delete user (fail)
        """
        response = self.client.delete('/api/users/1')
        self.assertEqual(response.status_code, 404)
