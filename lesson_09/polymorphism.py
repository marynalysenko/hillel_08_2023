# print( 1+ 1)
# print( '1'+ '1')

from functools import (  # регистрация функции в зависимости от типа входящих данных
    singledispatch,
)


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupporded type")  # fallback solution


@add.register(int)
def _(a, b):
    return a + b


@add.register(str)
def _(a, b):
    return f"Concat {a}{b}"


print(add(1, 1))
print(add("1", "1"))
# print( add(1.0, 1.0))


class User:
    name: str
    password: str


class Anonymous:
    geo: list


class Backend:
    @singledispatch
    def get_admin_pade(self, user):
        # reise NotImplementedError
        return "Not Enough"

    @get_admin_pade.register
    def _(user: User):
        return "ok"  # admin_page
