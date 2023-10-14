#!/usr/bin/python3
"""Test User class"""

from tests.test_models.test_base_model import TestBaseModel
from models.user import User

class TestUser(TestBaseModel):
    """Test the User class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = "User"
        self.base_model_instance = User

    def test_first_name(self):
        """Test the first_name attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.first_name), str)

    def test_last_name(self):
        """Test the last_name attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.last_name), str)

    def test_email(self):
        """Test the email attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.email), str)

    def test_password(self:
        """Test the password attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.password), str)

