from abc import ABC, abstractmethod

from observable import WeatherData


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(cls):
        pass


class BaseDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, data):
        if isinstance(data, WeatherData):  # запрос данных
            self.data = data.get_data()
        else:  # активная доставка
            self.data = data
        self.display()

    def display(self):
        print(self.__class__.__name__, self.data)


class ConditionsDisplay(BaseDisplay):
    pass


class StatisticsDisplay(BaseDisplay):
    pass


class ForecastDisplay(BaseDisplay):
    pass
