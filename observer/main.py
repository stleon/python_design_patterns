from data import Data
from observable import WeatherData
from observer import ConditionsDisplay, StatisticsDisplay, ForecastDisplay


if __name__ == '__main__':

    weather_data = WeatherData()
    for display in (ConditionsDisplay, StatisticsDisplay, ForecastDisplay):
        display(weather_data)

    weather_data.set_measurements(Data(80, 65, 30.4))
    weather_data.set_measurements(Data(82, 70, 29.2))
    weather_data.set_measurements(Data(78, 90, 29.2))
