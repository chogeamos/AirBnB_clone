#!/usr/bin/python3
"""Test City class"""

from tests.test_models.test_base_model import TestBaseModel
from models.city import City

class TestCity(TestBaseModel):
    """Test the City class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = "City"
        self.base_model_instance = City

    def test_state_id(self):
        """Test the state_id attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.state_id), str)

    def test_name(self):
        """Test the name attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.name), str)

