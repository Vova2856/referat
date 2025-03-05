Неправильний:
class Bird:
    def fly(self):
        print("Летить")

class Penguin(Bird):
    def fly(self):
        raise Exception("Пінгвін не літає")
bird = Bird()
bird.fly()  # Виведе: Летить


penguin = Penguin()
try:
    penguin.fly()
except Exception as e:
    print(e)