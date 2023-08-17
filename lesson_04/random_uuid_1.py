# A Universally Unique Identifier (UUID) is a 128-bit label used
# for information in computer systems.
# The term Globally Unique Identifier (GUID)
# is also used, mostly in Microsoft systems.
# Universally unique identifier.
# UUID/GUID as used by UEFI variables.

# The example UUID 123e4567-e89b-12d3-a456-426655440000

from uuid import UUID, uuid4

used_uuids = set()  # множини в пайтоні - це структура даних хеш-таблиць


def generate_unique_uuid() -> UUID:
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids:
            used_uuids.add(generated_uuid)
            return generated_uuid


print(generate_unique_uuid())
print(generate_unique_uuid())
print(generate_unique_uuid())
print(generate_unique_uuid())
print(generate_unique_uuid())

# 62efa01f-3b4f-4ed3-82fe-19ea9fda1a2b
# 78c62e25-3dfc-43cc-8830-631c069cf11e
# 954a8c28-73da-49a2-9981-0cbb21db80b0
# b9c49906-dcd2-4bbc-b5d0-b7de8fb8ee57
# a43c95c0-510b-4377-bbe8-334c7d89e22f
