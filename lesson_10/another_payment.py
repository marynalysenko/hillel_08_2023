# Імпортуємо необхідні класи для створення абстрактних класів
from abc import ABC, abstractmethod

# Абстрактний клас PaymentStrategy визначає інтерфейс для стратегій оплати
class PaymentStrategy(ABC):
    # Абстрактний метод для обробки платежу
    @abstractmethod
    def process_payment(self, amount: int):
        pass

    # Абстрактний метод для відображення типу платежу
    @abstractmethod
    def display_payment(self):
        pass

    # Метод для застосування знижки до суми платежу
    def apply_discount(self, amount: int, percentage: int):
        discount = (percentage / 100) * amount
        return int(amount - discount)

# Клас CreditCard є конкретною реалізацією стратегії оплати
class CreditCard(PaymentStrategy):
    # Обробка платежу з використанням кредитної картки
    def process_payment(self, amount: int):
        # Застосовуємо знижку в 5% до суми платежу
        amount = self.apply_discount(amount, 5)

        print(f"Processing credit card payment of ${amount}")

    # Відображення типу платежу
    def display_payment(self):
        print("Credit card payment")

# Функція payment_processor приймає стратегію оплати і обробляє платіж
def payment_processor(strategy: PaymentStrategy):
    strategy.process_payment(100)
    print("Payment processor is Done")

# Здійснюємо платіж з використанням стратегії оплати кредитною карткою
payment_processor(strategy=CreditCard())
