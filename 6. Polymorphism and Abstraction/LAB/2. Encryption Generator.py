class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other: int):
        if not isinstance(other, int):
            raise ValueError('You must add a number.')

        result = ''
        for el in self.text:
            ch_num = ord(el) + other
            if ch_num < 32:
                ch_num += 95
            if ch_num > 126:
                ch_num -= 95
            result += chr(ch_num)

        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
