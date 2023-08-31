# Цей приклад ілюструє використання декораторів @property, @setter та @deleter
# для реалізації інкапсуляції в ООП.
# Зокрема, ці декоратори дозволяють створити "публічний" інтерфейс
# для доступу до "приватних" атрибутів об'єкта.


class PaymentSystem:
    def __init__(self) -> None:
        # Встановлення атрибута, який показує, чи під'єднані ми до банкомату
        self.connected_to_the_atm: bool = False
        # Встановлення атрибута депозиту як "приватного" за допомогою двох підкреслень
        # перед його назвою
        self.__deposit = 0

    # getter - спеціальний декоратор, який дозволяє отримувати значення атрибута через
    # його "публічний" інтерфейс
    @property
    def deposit(self):
        return self.__deposit

    # setter - спеціальний декоратор, який дозволяє встановлювати значення атрибута
    # через його "публічний" інтерфейс
    @deposit.setter
    def deposit(self, value: int):
        self.__deposit += value

    # deleter - спеціальний декоратор, який викликається при спробі видалити атрибут
    @deposit.deleter
    def deposit(self):
        print("Can not delete the object")


# Створюємо екземпляр класу
privat = PaymentSystem()
# Отримуємо значення атрибута deposit за допомогою getter'а
print(privat.deposit)
# Встановлюємо значення атрибута deposit за допомогою setter'а
privat.deposit = 12
privat.deposit = 12
# Отримуємо знову значення атрибута deposit
print(privat.deposit)

# Наступні команди закоментовані:
# a = getattr(privat, "depositssss", None)  # Спроба отримати значення неіснуючого
# атрибута за допомогою функції getattr
# setattr(privat, "deposit", 30)  # Спроба встановити значення атрибута deposit
# за допомогою функції setattr
# delattr(privat, "deposit")  # Спроба видалити атрибут deposit за допомогою
# функції delattr
# del privat.deposit  # Спроба видалити атрибут deposit безпосередньо
