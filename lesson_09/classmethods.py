import random
import string


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @classmethod
    def create_with_temp_password(cls, username: str):
        temp_chars = [random.choice(string.ascii_letters) for _ in range(10)]
        temp_password = "".join(temp_chars)

        return cls(username=username, password=temp_password)


john = User(username="J", password="123")
john = User.create_with_temp_password(username="J")
