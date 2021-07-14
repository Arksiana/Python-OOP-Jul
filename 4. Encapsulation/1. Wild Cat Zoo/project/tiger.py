from project.animal import Animal


class Tiger(Animal):
    needs = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    @staticmethod
    def get_needs():
        return Tiger.needs
