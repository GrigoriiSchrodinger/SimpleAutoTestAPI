import unittest

import requests

from src.api.endpoint import EndPoints
from src.api.models.Users import User
from src.generate_string import generate_random_string


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://reqres.in"

    def test_create_user(self):
        user = User(name=generate_random_string(8), job="leader")
        response = requests.post(url=self.base_url + EndPoints.CREATE_USER, json=user.post_body())
        self.assertEqual(response.status_code, 201)
