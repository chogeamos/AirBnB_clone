#!/usr/bin/python3
"""Test State class"""

from tests.test_models.test_base_model import TestBaseModel
from models.state import State

class TestState(TestBaseModel):
    """Test the State class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = "State"
        self.base_model_instance = State

    def test_name(self):
        """Test the name attribute"""
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.name), str)

