#!/usr/bin/python3
"""Test Review class"""

from tests.test_models.test_base_model import TestBaseModel
from models.review import Review

class TestReview(TestBaseModel):
    """Test the Review class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = "Review"
        self.base_model_instance = Review

    def test_place_id(self):
        """Test the place_id attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.place_id), str)

    def test_user_id(self):
        """Test the user_id attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.user_id), str)

    def test_text(self):
        """Test the text attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.text), str)

