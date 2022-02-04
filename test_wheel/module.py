class Operator:
    def __init__(self, num1: int, num2: int) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def substract(self):
        return self.num1 - self.num2

    def times(self):
        return self.num1 * self.num2

    def divide_by(self):
        return self.num1 / self.num2
