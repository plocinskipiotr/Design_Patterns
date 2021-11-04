"""
This bidirectional adapter adapts json data in xml weather
class functionality and xml data in json weather class functionality
"""

import xmltodict
from dict2xml import dict2xml

from ijson_weather import IJsonWeather
from ixml_weather import IXmlWeather
from xml_weather import XmlWeather
from json_weather import JsonWeather


class JsonXmlAdapter(IJsonWeather, IXmlWeather):
    """Bidirectional adapter class for JSONs and XMLs """

    def __init__(self, xml, json):
        """
            Creating XmlWeather object with json data (adapts)
            and
            creating JsonWeather object with xml data (adapts)
        """
        self.xml_weather = XmlWeather(self._convert_json_to_xml_to_dict(json))
        self.json_weather = JsonWeather(self._convert_xml_to_json(xml))

    @staticmethod
    def _convert_json_to_xml_to_dict(json):
        """Converts json to xml to dict"""
        data = dict2xml(json)
        return xmltodict.parse(data)

    @staticmethod
    def _convert_xml_to_json(xml):
        """Converts xml to json"""
        return xmltodict.parse(xml)

    def get_icon(self):
        """Getting icon from xml"""
        return self.xml_weather.get_icon()

    def get_humidity(self):
        """Getting humidity from xml"""
        return self.xml_weather.get_humidity()

    def get_condition(self):
        """Getting condition from json"""
        return self.json_weather.get_condition()

    def get_pressure(self):
        """Getting pressure from json"""
        return self.json_weather.get_pressure()
