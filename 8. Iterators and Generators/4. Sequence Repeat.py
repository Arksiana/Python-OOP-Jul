class sequence_repeat:
    def __init__(self, text, repeat):
        self.text = text
        self.repeat = repeat
        self.index = 0
        self.index_text = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.repeat:
            raise StopIteration
        if self.index_text >= len(self.text):
            self.index_text = 0
        value = self.text[self.index_text]
        self.index_text += 1
        self.index += 1

        return value
