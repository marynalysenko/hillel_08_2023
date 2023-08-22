# сінгл тон (частіше за все з конекшенами використовуються)
class Person:
    _instance = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance  # Return the instance you've created

    def __init__(self, name: str, age: int) -> None:
        if self._initialized:
            return

        self.name: str = name
        self.age: int = age
        self._initialized = True

    @property
    def is_adult(self) -> bool:
        if self.age < 18:
            return False
        return True

    @is_adult.setter
    def is_adult(self, value: bool) -> None:
        print("It is not possible to override")

    @staticmethod
    def greeting(name: str):
        print(f"Hello from Person! Name: {name}")


john = Person(name="John", age=31)
mary = Person(name="Mary", age=27)

print(john.is_adult)

john.is_adult = False

# @lru_cache - подивитись
