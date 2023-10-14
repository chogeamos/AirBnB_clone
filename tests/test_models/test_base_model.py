#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
import datetime
import json
import os

class TestBaseModel(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = 'BaseModel'
        self.base_model_instance = BaseModel

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        instance = self.base_model_instance()
        self.assertEqual(type(instance), self.base_model_instance)

    def test_kwargs(self):
        instance = self.base_model_instance()
        data = instance.to_dict()
        new_instance = BaseModel(**data)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        instance = self.base_model_instance()
        data = instance.to_dict()
        data.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**data)

    def test_save(self):
        instance = self.base_model_instance()
        instance.save()
        key = self.q + "." + instance.id
        with open('file.json', 'r') as file:
            json_data = json.load(file)
            self.assertEqual(json_data[key], instance.to_dict())

    def test_str(self):
        instance = self.base_model_instance()
        self.assertEqual(
            str(instance),
            '[{}] ({}) {}'.format(self.q, instance.id, instance.__dict__)
        )

    def test_to_dict(self):
        instance = self.base_model_instance()
        instance_data = instance.to_dict()
        self.assertEqual(instance.to_dict(), instance_data)

    def test_kwargs_none(self):
        invalid_data = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.base_model_instance(**invalid_data)

    def test_kwargs_one(self):
        invalid_data = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new_instance = self.base_model_instance(**invalid_data)

    def test_id(self):
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.id), str)

    def test_created_at(self):
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.created_at), datetime.datetime)

    def test_updated_at(self):
        new_instance = self.base_model_instance()
        self.assertEqual(type(new_instance.updated_at), datetime.datetime)
        instance_data = new_instance.to_dict()
        new_instance = BaseModel(**instance_data)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)

