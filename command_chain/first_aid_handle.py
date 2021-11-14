"""first aid handle"""

from ihandler import IHandler


class FirstAidHandle(IHandler):
    """first aid handle"""

    def __init__(self, handler=None, request=None):
        self.next_handler = handler
        self.request = request

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        print("request received: " + request + ' by ' + FirstAidHandle.__name__)
        if request == "isWounded":
            print("Wounded is aided, request terminated")
        else:
            if self.next_handler:
                print("moved to next handler " + str(self.next_handler))
                self.next_handler.handle(request)
            else:
                print("end of chain reached request: " + request + " did not handle")

    def __str__(self):
        return FirstAidHandle.__name__
