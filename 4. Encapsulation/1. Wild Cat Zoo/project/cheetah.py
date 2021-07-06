from project.animal import Animal


class Cheetah(Animal):
    needs = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    @staticmethod
    def get_needs():
        return Cheetah.needs
