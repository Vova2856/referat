Неправильний:
class MySQL:
    def connect(self):
        print("Підключення до MySQL")

class App:
    def __init__(self):
        self.db = MySQL()

    def start(self):
        self.db.connect()


app = App()


app.start()
