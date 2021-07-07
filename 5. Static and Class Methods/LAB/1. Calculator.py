from functools import reduce


class Calculator:

    @classmethod
    def add(cls, *args):
        return sum(args)

    @classmethod
    def multiply(cls, *args):
        return reduce(lambda x, y: x * y, args)

    @classmethod
    def divide(cls, *args):
        return reduce(lambda x, y: x / y, args)

    @classmethod
    def subtract(cls, *args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))