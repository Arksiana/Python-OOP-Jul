from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        p_obj = [el for el in self.products if el.name == product_name][0]
        return p_obj

    def remove(self, product_name:str):

        for p_obj in self.products:
            if p_obj.name == product_name:
                self.products.remove(p_obj)

    def __repr__(self):
        result = []
        for el in self.products:
            result.append(f'{el.name}: {el.quantity}')
        return '\n'.join(result)

