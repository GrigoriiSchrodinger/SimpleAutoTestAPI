from src.utils.generate_string import generate_random_string


class User:
    def __init__(
            self,
            name=generate_random_string(8),
            job="leader",
            email=generate_random_string(4) + "." + generate_random_string(4) + "@reqres.in",
            password=generate_random_string(8)
    ):
        self.name = name,
        self.job = job,
        self.email = email
        self.password = password

    def post_body_create(self) -> dict:
        return dict(
            name=self.name,
            job=self.job,
        )

    def post_body_register(self) -> dict:
        return dict(
            email=self.email,
            password=self.password,
        )
