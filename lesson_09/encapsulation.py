from typing import Any


class User:
    def __init__(self, username: str, password: str):
        self.username: str = username
        self._password: str = password
        self._autorized: bool = False

    def __getattribute__(self, name: str) -> Any:
        if name == "password":
            return "Access Denied!"
        return super().__getattribute__(name)

    def login(self, username: str, password: str) -> None:
        if self.username == username and self._password == password:
            self._autorized = True
        else:
            self._autorized = False

    @property  # вона ігнорується бо перехопив __getattribute__ і повернув просто строку
    def password(self):
        return "******"

    def is_autorized(self) -> bool:
        return self._autorized


def login(username: str, password: str):
    john.login(username, password)
    if john.is_autorized:
        print("Success")
    else:
        print("Not Success")


john = User(username="John", password="12345")

login("John", "12345")
