# Кожен об'єкт у Python має властивість __dict__,
# яка представляє всі його атрибути у вигляді словника.
# У цьому прикладі ми створюємо екземпляр класу Person,
# додаємо до нього атрибути "name" та "age"
# і демонструємо ці атрибути за допомогою __dict__.


# Змінна / інстанс (екземпляр класу) / ентіті (кастомні класи з атрибутами)
# Коли ми створюємо новий екземпляр класу, спочатку викликається метод `__new__`,
# який відповідає за створення нового об'єкта. Після того, як `__new__` відпрацює,
# інтерпретатор викликає `__init__`, який ініціалізує об'єкт і наділяє його атрибутами.


# Визначення класу "Person"
class Person:
    # Конструктор класу, який викликається при створенні екземпляра класу
    def __init__(self) -> None:
        pass


# Створення екземпляра класу "Person"
john = Person()
# Виведення атрибутів екземпляра класу "john" у вигляді словника
# за допомогою властивості `__dict__`
print(john.__dict__)
# Додавання атрибута "name" до екземпляра "john"
john.name = "John"
# Додавання атрибута "age" до екземпляра "john"
john.age = 12
# Знову виведення атрибутів екземпляра класу "john"
print(john.__dict__)
# всі атрибути об'єкта представлені у вигляді словника
# (ключ - назва атрибута, значення - його значення)
