"""
Television Device
"""

from idevice import IDevice


class TV(IDevice):
    """ Television Device """

    def __init__(self, enabled=True, channel=1, volume=50):
        self.enabled = enabled
        self.channel = channel
        self.volume = volume

    def is_enabled(self):
        print("TV: " + str(self.enabled))
        return self.enabled

    def enable(self):
        self.enabled = True
        print("TV: " + str(self.enabled))

    def disable(self):
        self.enabled = False
        print("TV: " + str(self.enabled))

    def get_volume(self):
        print("TV: " + str(self.volume))
        return self.volume

    def get_channel(self):
        print("TV: " + str(self.channel))
        return self.channel

    def set_channel(self, value):
        self.channel = value
