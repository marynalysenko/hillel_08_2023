import time
from typing import Callable


def perf_counter(func: Callable):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        exec_time = time.perf_counter() - start
        print(f"Execution time: {exec_time:.6f} seconds")
        return (
            result  # You should return the result from the decorated function
        )

    return inner


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
        return self.age >= 18

    @is_adult.setter
    def is_adult(self, value: bool) -> None:
        print("It is not possible to override the 'is_adult' property")

    @perf_counter
    @staticmethod
    def greeting(name: str):
        print(f"Hello from Person! Name: {name}")


john = Person(name="John", age=31)
mary = Person(name="Mary", age=27)

print(john.is_adult)

john.is_adult = False

john.greeting()

# @lru_cache - подивитись
