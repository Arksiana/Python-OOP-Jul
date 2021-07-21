# TODO 75/100

from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory

class TestPaintFactory(TestCase):

    def setUp(self):
        self.paint_factory = PaintFactory('Factory', 50)

    def test_initial_atributtes(self):
        self.assertEqual('Factory', self.paint_factory.name)
        self.assertEqual(50, self.paint_factory.capacity)
        # self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertDictEqual({}, self.paint_factory.ingredients)
        self.assertDictEqual({}, self.paint_factory.products)

    def test_add_method_invalid_ingredient(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient('orange', 20)
        self.assertEqual("Ingredient of type orange not allowed in PaintFactory", str(context.exception))

    def test_add_method_invalid_quantity(self):
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('green', 55)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_add_method_valid_ingredient_and_quantity(self):
        self.paint_factory.add_ingredient('green', 25)
        self.paint_factory.add_ingredient('white', 25)
        self.assertEqual({'green': 25, 'white': 25}, self.paint_factory.ingredients)

    def test_remove_method_invalid_ingredient(self):
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient('orange', 20)
        self.assertEqual("No such ingredient in the factory", context.exception.args[0])

    def test_remove_method_invalid_quantity(self):
        self.paint_factory.add_ingredient('green', 25)
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient('green', 30)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_method_valid_ingredient_and_quantity(self):
        self.paint_factory.add_ingredient('green', 25)
        self.paint_factory.remove_ingredient('green', 25)
        self.assertEqual({'green': 0}, self.paint_factory.ingredients)

    def test_products_property(self):
        self.paint_factory.add_ingredient('green', 25)
        self.paint_factory.add_ingredient('white', 25)
        self.assertEqual({'green': 25, 'white': 25}, self.paint_factory.ingredients)

    def test_can_add_method_false_from_base_class(self):
        self.paint_factory.add_ingredient('green', 20)
        self.paint_factory.add_ingredient('white', 20)
        self.assertTrue(self.paint_factory.can_add(10))

    def test_can_add_method_true_from_base_class(self):
        self.paint_factory.add_ingredient('green', 25)
        self.paint_factory.add_ingredient('white', 25)
        self.assertFalse(self.paint_factory.can_add(10))


if __name__ == '__main__':
    main()