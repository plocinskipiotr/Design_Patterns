"""
Main loop for adapter example
"""
from json import load
from adapter import JsonXmlAdapter

JSON_PATH = r'data/adapterweather.json'
XML_PATH = r'data/adapterweather.xml'

if __name__ == '__main__':
    with open(file=JSON_PATH, mode='r') as f:
        json_data = load(f)

    with open(file=XML_PATH, mode='r') as f:
        xml_data = f.read()

    adapter = JsonXmlAdapter(xml_data, json_data)
    a = adapter.get_icon()
    b = adapter.get_humidity()
    c = adapter.get_condition()
    d = adapter.get_pressure()

    print(a + '\n' + b + '\n' + c + '\n' + d)
