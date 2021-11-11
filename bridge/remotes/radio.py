"""
Radio Device
"""

from idevice import IDevice


class Radio(IDevice):
    """ Radio Device """

    def __init__(self, enabled=True, channel=1, volume=50):
        self.enabled = enabled
        self.channel = channel
        self.volume = volume

    def is_enabled(self):
        print("Radio: " + str(self.enabled))
        return self.enabled

    def enable(self):
        self.enabled = True
        print("Radio: Enabled")

    def disable(self):
        self.enabled = False
        print("Radio: Disabled")

    def get_volume(self):
        print("Radio: " + str(self.volume))
        return self.volume

    def get_channel(self):
        print("Radio: " + str(self.channel))
        return self.channel

    def set_channel(self, value):
        self.channel = value
