class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.index:
            raise StopIteration
        temp_num = self.value
        self.index += 1
        self.value += self.step

        return temp_num



numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
