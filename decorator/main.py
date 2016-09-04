from beverage import *
from wrapper import *

if __name__ == '__main__':
    beverage = Expresso()
    print(beverage)

    beverage2 = DarkRoast()
    for wr in (Mocha, Mocha, Whip):
        beverage2 = wr(beverage2)
    print(beverage2)

    beverage3 = HouseBlend()
    for wr in (Soy, Mocha, Whip):
        beverage3 = wr(beverage3)
    print(beverage3)
