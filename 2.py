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