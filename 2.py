Неправильний:
class Payment:
    def pay(self, method):
        if method == "card":
            print("Оплата картою")
        elif method == "paypay":
            print("Оплата PayPay")


payment = Payment()
payment.pay("card")
payment.pay("paypay")
payment.pay("cash")





Правильний:
class Payment:
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        print("Оплата карткою")

class PayPalPayment(Payment):
    def pay(self):
        print("Оплата PayPal")

def process_payment(payment):
    payment.pay()

process_payment(CardPayment())
process_payment(PayPalPayment())
