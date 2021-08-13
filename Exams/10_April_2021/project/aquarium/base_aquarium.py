from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        # result = 0
        # for dec in self.decorations:
        #     result += dec.comfort
        return sum([dec.comfort for dec in self.decorations])

    def add_fish(self, fish):
        if self.capacity <= 0:
            return "Not enough capacity."
        map_fish_type = ["FreshwaterFish", "SaltwaterFish"]
        if fish.__class__.__name__ in map_fish_type:
            self.fish.append(fish)
            self.capacity -= 1
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        for el in self.fish:
            if el.name == fish.name:
                self.fish.remove(el)
                self.capacity += 1

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fi in self.fish:
            fi.eat()

    def __str__(self):
        res = []
        res.append(f"{self.name}:")
        fishes = [el.name for el in self.fish]
        res.append(f"Fish: {' '.join(fishes) if fishes else 'none'}")
        res.append(f"Decorations: {len(self.decorations)}")
        res.append(f"Comfort: {self.calculate_comfort()}")

        return res


