class User:
    def __init__(self, name):
        self.name = name

    def save(self):
        print(f"Зберігаю {self.name}")

    def send_email(self):
        print(f"Надсилаємо лист {self.name}")


user = User("Вова")


user.save()
user.send_email()
