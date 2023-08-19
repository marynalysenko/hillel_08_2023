from pprint import pprint as print

print("Marie")
print(repr("John"))


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self):
        """Magic method for object representation."""
        return f"{self.name} representation"

    def __str__(self):
        """Magic method for string representation."""
        return f"{self.name} string representation"

    def another(self):
        return "from another"


john = Person(name="John")

print("*******************************************************")

# Working with booleans
john_contact_info_existance = (True, True, False, False, True, False, True)
print(john_contact_info_existance)

# Check if all fields are filled
for item in john_contact_info_existance:
    if not item:
        print("Some fields do not exist")
        break

if not all(john_contact_info_existance):
    print("Some fields do not exist")

if any(john_contact_info_existance):
    print("At least one field does exist")

print("*******************************************************")

team = ["John", "Jack", "Rosa", "Mark", "Marry"]
print(team)
print(sorted(team))
print(sorted(team, reverse=True))

print("*******************************************************")

team = ["John", "jack", "Rosa", "Mark", "Marry"]
print(team)
print(sorted(team))
print(sorted(team, reverse=True))
print(ord("J"))
print(chr(74))

print("*******************************************************")

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Rosa", "age": 30, "number": 18},
    {"name": "Mark", "age": 20, "number": 13},
]


def by_age(item: dict):
    return item["age"]


print(sorted(team, key=by_age))

print("*******************************************************")

print(sorted(team, key=lambda item: item["age"]))
