# приклад з конкретними юзерами
from typing import Generator, Set
from uuid import UUID, uuid4

used_uuids_by_user: dict[str, Set[UUID]] = {}


def generate_unique_uuid(user: str) -> Generator[UUID, None, None]:
    while True:
        generated_uuid = uuid4()

        if user not in used_uuids_by_user:
            used_uuids_by_user[user] = set()

        if generated_uuid not in used_uuids_by_user[user]:
            used_uuids_by_user[user].add(generated_uuid)
            yield generated_uuid


john_unique_uuid = generate_unique_uuid("John")
mary_unique_uuid = generate_unique_uuid("Mary")

print(next(john_unique_uuid))
print(next(john_unique_uuid))
print(next(john_unique_uuid))
print(next(mary_unique_uuid))
