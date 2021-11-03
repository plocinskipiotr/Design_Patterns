"""
Json weather class
"""

from json import load


class json_weather_class():
    def __init__(self):
        self.json_file = './adapterweather.json'

    def get_pressure(self):
        with open(file=self.json_file, mode='r', ) as f:
            data = load(f)
            return data['weather']['pressure_msl']

    def get_temperature(self):
        with open(file=self.json_file, mode='r', ) as f:
            data = load(f)
            return data['weather']['temperature']
