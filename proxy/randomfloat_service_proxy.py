"""Generate Random Float Proxy"""

from iservice import IService

REQ_NUMBER_LIMIT = 10


class RandomFloatServiceProxy(IService):
    """Generate Random Float Proxy"""

    def __init__(self, service, req_number=0):
        self.service: IService = service
        self.req_number = req_number

    def _check_access(self):
        """access control for service"""
        return self.req_number < REQ_NUMBER_LIMIT

    def get_data(self):
        """getting data"""
        self.req_number += 1
        if self._check_access():
            return self.service.get_data()
        print('request denied, too many requests (' + str(self.req_number) + ')')
        return -1
