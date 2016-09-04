from beverage import Beverage


class Wrapper(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return '%s, %s' % (self.beverage.get_description(),
                           self.__class__.__name__)


class Mocha(Wrapper):
    def cost(self):
        return .20 + self.beverage.cost()


class Soy(Wrapper):
    def cost(self):
        return .15 + self.beverage.cost()


class Whip(Wrapper):
    def cost(self):
        return .10 + self.beverage.cost()
