"""
Xml weather class
"""

import xmltodict


class xml_weather_class():
    def __init__(self):
        self.xml_file = './adapterweather.xml'

    def get_icon(self):
        with open(file=self.xml_file, mode='r', ) as f:
            data = xmltodict.parse(f.read())
            return data['root']['weather']['icon']

    def get_humidity(self):
        with open(file=self.xml_file, mode='r', ) as f:
            data = xmltodict.parse(f.read())
            return data['root']['weather']['relative_humidity']
