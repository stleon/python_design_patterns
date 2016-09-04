from abc import ABC, abstractmethod


class Beverage(ABC):
    def __str__(self):
        return '%s, $%s' % (self.get_description(), self.cost())

    @abstractmethod
    def cost(self):
        pass

    def get_description(self):
        return self.description


class Expresso(Beverage):
    def __init__(self):
        self.description = "Expresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return .99
