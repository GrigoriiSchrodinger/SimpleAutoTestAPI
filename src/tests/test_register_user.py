import unittest
import requests
import json

from src.api.endpoint import EndPoints
from src.api.models.Users import User
from jsonschema import validate


class TestRegisterUser(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = "https://reqres.in"

    def test_register_successful(self) -> None:
        response = requests.post(
            url=self.base_url + EndPoints.REGISTER_USER,
            json=User(email="eve.holt@reqres.in", password="pistol").post_body_register()
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

    def test_register_unsuccessful(self) -> None:
        response = requests.post(
            url=self.base_url + EndPoints.REGISTER_USER,
            json=User(email="eve.holt@reqres.in", password=None).post_body_register()
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Missing password")

    def test_register_successful_scheme(self) -> None:
        with open("src/api/schemas/register_user.json", "r") as schema_file:
            schema = json.load(schema_file)

        response = requests.post(
            url=self.base_url + EndPoints.REGISTER_USER,
            json=User(email="eve.holt@reqres.in", password="pistol").post_body_register()
        )

        # Проверка соответствия ответа схеме
        validate(instance=response.json(), schema=schema)



