"""base handle"""

from ihandler import IHandler


class BaseHandler(IHandler):
    """base handle"""

    def __init__(self, handler=None, request=None):
        self.next_handler = handler
        self.request = request

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        print("request received: " + request + ' by ' + BaseHandler.__name__)
        if self.next_handler:
            print("moved to next handler " + str(self.next_handler))
            self.next_handler.handle(request)
        else:
            print("end of chain reached request: " + request + " did not handle")

    def __str__(self):
        return BaseHandler.__name__
