from typing import Generator, Set
from uuid import UUID, uuid4

used_uuids: Set[UUID] = set()  # Using a set to store used UUIDs


def generate_unique_uuid() -> Generator[UUID, None, None]:
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids:
            used_uuids.add(generated_uuid)
            yield generated_uuid


# Initializing the generator
uuid_generator = generate_unique_uuid()

print(next(uuid_generator))
print(next(uuid_generator))
print(next(uuid_generator))

print(used_uuids)
