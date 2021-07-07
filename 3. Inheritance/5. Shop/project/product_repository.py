from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = [el for el in self.products if el.name == product_name][0]
        return product

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = []
        for el in self.products:
            result.append(f'{el.name}: {el.quantity}')
        return '\n'.join(result)

