from abc import ABC, abstractmethod

from fly_behavior import *
from quack_behavior import *


class Duck(ABC):

    fly_behavior = None
    quck_behavior = None

    @abstractmethod
    def display(self):
        pass

    def swim(self):
        print("All ducks swim")

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quck_behavior = qb

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quck_behavior.quack()


class MallardDuck(Duck):

    fly_behavior = FlyWithWings()
    quck_behavior = Quack()

    def display(self):
        print("I am a real Mallard duck")


class ReadHeadDuck(Duck):

    fly_behavior = FlyWithWings()
    quck_behavior = Quack()

    def display(self):
        print("I am a real Red head duck")


class RubberDuck(Duck):

    fly_behavior = FlyNoWay()
    quck_behavior = Squeak()

    def display(self):
        print("I am a Rubber duck")


class ModelDuck(Duck):

    fly_behavior = FlyNoWay()
    quck_behavior = MuteQuack()

    def display(self):
        print("I am a model duck")
