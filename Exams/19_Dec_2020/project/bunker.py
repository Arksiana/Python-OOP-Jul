from project.medicine.medicine import Medicine
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [el for el in self.supplies if el.__class__.__name__ == 'FoodSupply']
        if not result:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = [el for el in self.survivors if el.__class__.__name__ == 'WaterSupply']
        if not result:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [el for el in self.survivors if el.__class__.__name__ == 'Painkiller']
        if not result:
            raise IndexError("There are no painkillers left!")
        return result

    @property
    def salves(self):
        result = [el for el in self.survivors if el.__class__.__name__ == 'Salve']
        if not result:
            raise IndexError("There are no salves left!")
        return result

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            for med in self.medicine[::-1]:
                if med.__class__.__name__ == medicine_type:
                    med.apply(survivor)
                    self.medicine.remove(med)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for sus in self.supplies[::-1]:
                if sus.__class__.__name__ == sustenance_type:
                    sus.apply(survivor)
                    self.supplies.remove(sus)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            FoodSupply().apply(survivor)
            WaterSupply().apply(survivor)

