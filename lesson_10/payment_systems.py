# Імпортуємо необхідні класи для створення абстрактних класів
from abc import ABC, abstractmethod

# Клас User представляє користувача з його основною інформацією
class User:
    def __init__(self, name, card_name, cvv):
        self.name = name
        self.card_name = card_name
        self.cvv = cvv

# Клас Product представляє продукт з його назвою та ціною
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Абстрактний клас PaymentSystem визначає інтерфейс для систем оплати
class PaymentSystem(ABC):
    @abstractmethod
    def checkout(self, product: Product, user: User):
        pass

# Клас PayPal є конкретною реалізацією системи оплати
class PayPal(PaymentSystem):
    def checkout(self, product: Product, user: User):
        print(
            f"Checking out with PayPal for {user.name}\n"
            f"The product: {product.name} [{product.price}]"
        )

# Клас Stripe також є конкретною реалізацією системи оплати
class Stripe(PaymentSystem):
    def checkout(self, product: Product, user: User):
        print(
            f"Checking out with Stripe for {user.name}\n"
            f"The product: {product.name} [{product.price}]"
        )

# Функція make_purchace дозволяє здійснити покупку, використовуючи конкретну систему оплати
def make_purchace(
    payment_system: PaymentSystem,
    product: Product,
    user: User,
):
    print(
        f"{user.name} making a purchace - {product.name} for {product.price} UAH"
    )
    payment_system.checkout(product=product, user=user)

# Створюємо об'єкти для демонстрації роботи коду
john = User(
    name="John",
    card_name="4444-1111-3333-5555",
    cvv="123",
)
paypal = PayPal()
stripe = Stripe()
shoes = Product(name="Adidas", price=5000)

# Здійснюємо покупку через різні системи оплати
make_purchace(
    user=john,
    payment_system=paypal,
    product=shoes,
)
make_purchace(
    user=john,
    payment_system=stripe,
    product=shoes,
)
