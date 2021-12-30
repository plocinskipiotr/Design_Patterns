"""food handle"""

from ihandler import IHandler


class FoodHandle(IHandler):
    """food handle"""

    def __init__(self, handler=None, request=None):
        self.next_handler = handler
        self.request = request

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        print("request received: " + request + ' by ' + FoodHandle.__name__)
        if request == "isHungry":
            print("food provided, request terminated")
        else:
            if self.next_handler:
                print("moved to next handler " + str(self.next_handler))
                self.next_handler.handle(request)
            else:
                print("end of chain reached request: " + request + " did not handle")

    def __str__(self):
        return FoodHandle.__name__
