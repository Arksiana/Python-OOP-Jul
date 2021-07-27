class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        self.index -= 1


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
