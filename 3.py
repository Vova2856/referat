Неправильний:
class Bird:
    def fly(self):
        print("Летить")

class Penguin(Bird):
    def fly(self):
        raise Exception("Пінгвін не літає")
bird = Bird()
bird.fly()


penguin = Penguin()
try:
    penguin.fly()
except Exception as e:
    print(e)








Правильний:
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Летить")

class Penguin(Bird):
    def move(self):
        print("Плаває")


bird = Bird()


bird.move()


penguin = Penguin()
penguin.move()


flying_bird = FlyingBird()
flying_bird.move()
