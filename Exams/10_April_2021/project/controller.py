from project.aquarium.freshwater_aqarium import FreshwaterAquarium
from project.aquarium.saltwater_aqarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository = []
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type != 'FreshwaterAquarium' or aquarium_type != 'SaltwaterAquarium':
            return "Invalid aquarium type."

        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))

        if aquarium_type == 'SaltwaterAquarium':
            self.aquariums.append(SaltwaterAquarium(aquarium_name))

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type != 'Ornament' and decoration_type != 'Plant':
            return "Invalid aquarium type."

        if decoration_type == 'Ornament':
            self.aquariums.append(Ornament())

        if decoration_type == 'SaltwaterAquarium':
            self.aquariums.append(Plant())

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        """"If there is such decoration and such aquarium, you should add the first occurrence of the
        desired decoration to the aquarium with the given name. You should remove the decoration from the
        DecorationRepository and return the following message:"""
        aquariums = [el for el in self.aquariums if el.name == aquarium_name]
        if aquariums:
            dec = self.decorations_repository.find_by_type(decoration_type)
            if dec == "None":
                return f"There isn't a decoration of type {decoration_type}."

            aquariums[0].add_decoration(dec)
            self.decorations_repository.remove(dec)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        """Creates a fish of the given type and adds it to the aquarium with the given name. Valid fish types are:
        "FreshwaterFish" and "SaltwaterFish". If the fish type is invalid, you should return a massage:"""
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        fish = FreshwaterFish(fish_name, fish_species, price) if fish_type == "FreshwaterFish" \
            else SaltwaterFish(fish_name, fish_species, price)
        aq = [a for a in self.aquariums if a.name == aquarium_name]
        if aq:
            msg = aq[0].add_fish(fish)
            if not msg:
                return "Water not suitable."
            return msg

    def feed_fish(self, aquarium_name):
        list_aq = [a for a in self.aquariums if a.name == aquarium_name]
        if list_aq:
            list_aq[0].feed()
            return f"Fish fed: {len(list_aq[0].fish)}"

    def calculate_value(self, aquarium_name):
        list_aq = [a for a in self.aquariums if a.name == aquarium_name]
        value = 0
        if list_aq:
            fish_pr = sum(f.price for f in list_aq[0].fish)
            dec_pr = sum(d.price for d in list_aq[0].decorations)
            value = fish_pr + dec_pr
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        for aqua in self.aquariums:
            result.append(str(aqua))
        return "\n".join(result)

