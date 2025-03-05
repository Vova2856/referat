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



Правильний:
class Database:
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Підключення до MySQL")

class App:
    def __init__(self, db):
        self.db = db

    def start(self):
        self.db.connect()


app = App(MySQL())


app.start()
