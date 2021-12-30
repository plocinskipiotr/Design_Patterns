"""Json weather class"""

from ijson_weather import IJsonWeather


class JsonWeather(IJsonWeather):
    """Json class gets data from json fields"""

    def __init__(self, data):
        self.data = data

    def get_pressure(self):
        """Getting pressure from json"""
        return self.data['root']['weather']['pressure_msl']

    def get_condition(self):
        """Getting condition from json"""
        return self.data['root']['weather']['condition']
