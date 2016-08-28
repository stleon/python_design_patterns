from abc import ABC, abstractmethod

from data import Data


class Observable(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherData(Observable):
    data = Data(None, None, None)

    def __init__(self):
        self.observers = set()

    def register_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_changed(self):
        self.changed = True

    def notify_observers(self, data=None):
        if self.changed:
            if data is None:  # запрос данных
                data = self
            for o in self.observers:
                o.update(data)
            self.changed = False

    def measurements_changed(self):
        self.set_changed()
        self.notify_observers()

    def set_measurements(self, data):
        WeatherData.data = data
        self.measurements_changed()

    @classmethod
    def get_data(cls):
        return cls.data
