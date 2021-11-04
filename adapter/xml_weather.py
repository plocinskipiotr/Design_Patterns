"""Xml weather class"""

from ixml_weather import IXmlWeather


class XmlWeather(IXmlWeather):
    """Xml class gets data from xml fields"""

    def __init__(self, data):
        self.data = data

    def get_icon(self):
        """Getting icon from xml"""
        return self.data['root']['weather']['icon']

    def get_humidity(self):
        """Getting relative humidity from xml"""
        return self.data['root']['weather']['relative_humidity']
