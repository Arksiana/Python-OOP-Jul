from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    WEIGHT = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Owl.WEIGHT * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += Hen.WEIGHT * food.quantity
        self.food_eaten += food.quantity
