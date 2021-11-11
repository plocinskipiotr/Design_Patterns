"""
Main loop for proxy example
"""
from randomfloat_service_proxy import RandomFloatServiceProxy
from randomfloat_service import RandomFloatService

if __name__ == '__main__':
    ProxyService = RandomFloatServiceProxy(RandomFloatService())

    for item in range(15):
        print('Generated number: ' + str(ProxyService.get_data()))
