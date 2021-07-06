from project.animal import Animal


class Lion(Animal):
    needs = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    @staticmethod
    def get_needs():
        return Lion.needs
