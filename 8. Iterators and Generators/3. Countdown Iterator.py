class countdown_iterator:
    def __init__(self, number):
        self.number = number
        self.index = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        self.index -= 1
        value = self.number
        self.number -= 1
        return value


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
