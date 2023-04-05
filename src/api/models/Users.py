class User:
    def __init__(self, name, job):
        self.name = name,
        self.job = job,

    def post_body(self) -> dict:
        return dict(
            name=self.name,
            job=self.job,
        )

