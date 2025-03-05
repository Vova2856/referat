Неправильний:
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






Правильний:
class User:
    def __init__(self, name):
        self.name = name

class UserSaver:
    def save(self, user):
        print(f"Зберігаю {user.name}")

class EmailSender:
    def send_email(self, user):
        print(f"Надсилаю лист {user.name}")



user = User("Вова")


user_saver = UserSaver()
user_saver.save(user)


email_sender = EmailSender()
email_sender.send_email(user)




