from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super(Tea, self).__init__(name, price, milliliters)