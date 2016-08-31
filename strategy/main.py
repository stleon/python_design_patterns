from duck import MallardDuck, ModelDuck
from fly_behavior import FlyRocketPowered

if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.perform_fly()
    mallard.perform_quack()

    print('=' * 50)

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()
