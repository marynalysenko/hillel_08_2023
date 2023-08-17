# функція приймає певні аргументи, має тіло
# Є орієнтовні на дані і є поведінкові функції
def foo():
    pass


# ми можемо повертати безліч обєктів
def foo2():
    return 1, 2, 3, 4, 5


data1, data2, data3, data4, data5 = foo2()

print(data1, data2, data3, data4, data5)

# данні повернуться як кортеж
data = foo2()
print(data)


def foo3():
    return (1,)  # кома в кінці заставляє повертати кортеж


data = foo3()
print(data)


# розпаковка

a, b, c = 10, 20, 30  # фактично тут знаходить кортеж (10,20,30)
# і при присвоюванні його перевіряють і засовують у відповідну змінну
# є перевірка на довжину
print(a, b, b)

contact_info = ("Marie", "Lio", "Dnipro", "52030", "+380677571213", "w", 26)
# name, surname,city,postal_code, phone, sex, age = contact_info
# print(name,city)

# можна розпакувати тільки ті що цікаві
name, surname, *meta, age = contact_info
print(name, surname, age)
print(meta)


def create_user(name, surname, city, postal_code, phone_number, sex, age):
    print("User is created")
    print(f"The name is {name}")
    print(f"The surname is {surname}")


create_user(
    name="John",
    surname="Doe",
    city="Kyiv",
    postal_code="33111",
    phone_number="+3801222234",
    sex="man",
    age=40,
)


def create_user2(*args, **kwargs):
    print("User is created")
    print(kwargs)


create_user2(
    name="John",
    surname="Doe",
    city="Kyiv",
    postal_code="33111",
    phone_number="+3801222234",
    sex="man",
    age=40,
)


# позиційні (ключові) і резинові аргументи
def create_user3(name, surname, city, **kwargs):
    print("User is created")
    print(kwargs)
    print(f"The name is {name}")
    print(f"The surname is {surname}")


create_user3(
    name="John",
    surname="Doe",
    city="Kyiv",
    postal_code="33111",
    phone_number="+3801222234",
    sex="man",
    age=40,
)
