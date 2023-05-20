import json
import unittest

import requests

from jsonschema import validate
from src.api.endpoint import EndPoints
from src.api.models.Users import User


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://reqres.in"

    def test_create_user(self):
        response = requests.post(
            url=self.base_url + EndPoints.CREATE_USER,
            json=User().post_body_create()
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

    def test_schema_create_user(self):
        with open("src/api/schemas/create_user.json", "r") as schema_file:
            schema = json.load(schema_file)

        response = requests.post(
            url=self.base_url + EndPoints.CREATE_USER,
            json=User().post_body_create()
        )

        # Проверка соответствия ответа схеме
        validate(instance=response.json(), schema=schema)

