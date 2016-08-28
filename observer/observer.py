from abc import ABC, abstractmethod

from data import Data
from observable import WeatherData


class Observer(ABC):

    @abstractmethod
    def update(self, data, observable=None):
        pass


class DisplayElement(ABC):

    @abstractmethod
    def display(cls):
        pass


class BaseDisplay(Observer, DisplayElement):
    data = Data(None, None, None)

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    @classmethod
    def update(cls, data):
        if isinstance(data, WeatherData):  # запрос данных
            cls.data = data.get_data()
        else:  # активная доставка
            cls.data = data
        cls.display()

    @classmethod
    def display(cls):
        print(cls.__name__, cls.data)


class ConditionsDisplay(BaseDisplay):
    pass


class StatisticsDisplay(BaseDisplay):
    pass


class ForecastDisplay(BaseDisplay):
    pass
