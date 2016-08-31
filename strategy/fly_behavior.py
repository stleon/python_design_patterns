from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cant fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I am flying with a rocket!")
