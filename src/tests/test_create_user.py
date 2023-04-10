import json
import unittest

import requests

from jsonschema import validate
from src.api.endpoint import EndPoints
from src.api.models.Users import User
from src.utils.generate_string import generate_random_string


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://reqres.in"

    def test_create_user(self):
        user = User(name=generate_random_string(8), job="leader")
        response = requests.post(url=self.base_url + EndPoints.CREATE_USER, json=user.post_body())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

    def test_schema_create_user(self):
        with open("src/api/schemas/create_user.json", "r") as scheme:
            schema = json.load(scheme)

        user = User(name=generate_random_string(8), job="leader")
        response = requests.post(url=self.base_url + EndPoints.CREATE_USER, json=user.post_body()).json()

        # Проверка соответствия ответа схеме
        validate(instance=response, schema=schema)

