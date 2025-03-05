неправильний:
class Printer:
    def print(self):
        pass

    def scan(self):
        pass

class SimplePrinter(Printer):
    def print(self):
        print("Друкую")

    def scan(self):
        raise Exception("Не вмію сканувати")


printer = SimplePrinter()


printer.print()


try:
    printer.scan()
except Exception as e:
    print(e)





Правильний:
class Printer:
    def print(self):
        pass  # Метод для друку

class Scanner:
    def scan(self):
        print("Сканую")

class SimplePrinter(Printer, Scanner):
    def print(self):
        print("Друкую")


printer = SimplePrinter()


printer.print()
printer.scan()
