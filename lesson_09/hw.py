class Price:
    exchange_rates_to_usd = {
        "USD": 1,
        "EUR": 0.93,
        "UAH": 36.92,
        "AZN": 1.70,
        "VND": 24057.5,
    }

    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = round(amount, 2)
        self.currency: str = currency
        print(f"🆕 Price instance created with {self.amount} {self.currency}")

    def _convert_to_usd(self, amount, currency):
        converted_amount = round(
            amount / self.exchange_rates_to_usd[currency], 2
        )
        print(f"🔁 Converted {amount} {currency} to {converted_amount} USD")
        return converted_amount

    def _convert_from_usd(self, amount, target_currency):
        converted_amount = round(
            amount * self.exchange_rates_to_usd[target_currency], 2
        )
        print(
            f"🔁 Converted {amount} USD to {converted_amount} {target_currency}"
        )
        return converted_amount

    def __add__(self, other):
        print(
            f"➕ Adding {self.amount} {self.currency} and {other.amount} {other.currency}"
        )
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)

        left_amount_in_usd = (
            self._convert_to_usd(self.amount, self.currency)
            if self.currency != "USD"
            else self.amount
        )
        right_amount_in_usd = (
            self._convert_to_usd(other.amount, other.currency)
            if other.currency != "USD"
            else other.amount
        )
        total_in_usd = left_amount_in_usd + right_amount_in_usd
        result_amount = self._convert_from_usd(total_in_usd, self.currency)
        return Price(result_amount, self.currency)

    def __sub__(self, other):
        print(
            f"➖ Subtracting {other.amount} {other.currency} from {self.amount} {self.currency}"
        )
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)

        left_amount_in_usd = (
            self._convert_to_usd(self.amount, self.currency)
            if self.currency != "USD"
            else self.amount
        )
        right_amount_in_usd = (
            self._convert_to_usd(other.amount, other.currency)
            if other.currency != "USD"
            else other.amount
        )
        diff_in_usd = left_amount_in_usd - right_amount_in_usd
        result_amount = self._convert_from_usd(diff_in_usd, self.currency)
        return Price(result_amount, self.currency)

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __repr__(self):
        return f"Price(amount={self.amount:.2f}, currency='{self.currency}')"


price1 = Price(100.0, "USD")
price2 = Price(1000.0, "UAH")
price3 = price1 + price2
price4 = price1 - price2

print(price3, price4)
