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

    @classmethod  # паттерн classmethod сьел self и вместо него подмешал cls
    def greeting(
        cls,
    ):
        print(f"hello from {cls}")


john = Person(name="John", age=31)
mary = Person(name="Mary", age=27)

print(john)
print(mary)

print(john.name, john.age)
print(mary.name, mary.age)

john.greeting()  # Person.greeting(john)
mary.greeting()
print(Person)
