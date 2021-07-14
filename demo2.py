class Mammal:
    __kindgom = "animals"

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    @staticmethod
    def get_kingdom():
        return Mammal.__kindgom

    def info(self):
        return f"{self.name} is of type {self.type}"