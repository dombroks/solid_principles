from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentManager(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class EmailAuthPayment(PaymentManager):
    def email_auth(self, code):
        pass

    def pay(self, order):
        pass


class DebitPayment(EmailAuthPayment):
    def __init__(self, security_code):
        self.security_code = security_code
        self.authorized = False

    def email_auth(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def pay(self, order):
        if not self.authorized:
            raise Exception("Not authorized to perform this operation")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPayment(PaymentManager):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPayment(PaymentManager):
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())

paymentManager = DebitPayment("549651984")
paymentManager.email_auth(9481818)
paymentManager.pay(order)
