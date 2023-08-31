# Основна ідея коду - демонстрація принципу інкапсуляції в ООП.
# Цей код обмежує доступ до "приватних" методів класу,
# якщо вони не додані до множини дозволених методів.
# Це реалізовано за допомогою перевизначення методу __getattribute__.

# Імпорт типу Any для анотації типів
from typing import Any

# Чорний список методів, доступ до яких зовні класу має бути обмежений
methods_blacklist = [
    "_connect_to_the_atm",
    "_count_the_cash",
    "_get_money",
]

# Множина дозволених методів для виклику
ALLOWED = set()


class PaymentSystem:
    def __init__(self) -> None:
        # Встановлення атрибута, який показує, чи під'єднані ми до банкомату
        self.connected_to_the_atm: bool = False

    # Перевизначення магічного методу __getattribute__, який викликається
    # при спробі доступу до будь-якого атрибута класу
    def __getattribute__(self, name: str) -> Any:
        print(f"Accessing the attribute: {name}")

        # Якщо назва атрибута знаходиться в чорному списку
        # і не є дозволеною, піднімати виключення
        if name in methods_blacklist and name not in ALLOWED:
            raise Exception(f"The attribute {name} is private")

        # Якщо назва атрибута дозволена, видаляємо її з множини дозволених
        try:
            ALLOWED.remove(name)
        except KeyError:
            pass

        # Повертаємо атрибут, використовуючи метод базового класу
        return object.__getattribute__(self, name)
        # return super().__getattribute__(name)

    # Публічний метод для депозиту
    def deposit(self, amount: int):
        pass

    # Приватний метод для підключення до банкомату
    def _connect_to_the_atm(self):
        self.connected_to_the_atm = True
        print("Connected to the ATM")

    # Приватний метод для підрахунку готівки в банкоматі
    def _count_the_cash(self, amount: int):
        print("Counting the cash in the ATM")
        print(f"Total: {amount}")

    # Приватний метод для видачі грошей користувачеві
    def _get_money(self):
        print("💸 Returning money to the user")

    # Публічний метод для зняття готівки
    def withdraw(self, amount: int):
        # Додаємо приватні методи до множини дозволених для цього конкретного виклику
        ALLOWED.add("_connect_to_the_atm")
        ALLOWED.add("_count_the_cash")
        ALLOWED.add("_get_money")

        self._connect_to_the_atm()
        self._count_the_cash(amount)
        self._get_money()


# Створюємо екземпляр класу
privat = PaymentSystem()
# privat.deposit(amount=100)   # Внесення готівки (цей рядок закоментований)
privat.withdraw(amount=100)  # Зняття готівки
# privat._PaymentSystem__get_money()   # Спроба виклику "приватного" методу
# privat._get_money()   # Спроба виклику "приватного" методу
# після його виклику в методі withdraw
