"""
Standard remote
"""

from iremote import IRemote
from idevice import IDevice


class StandardRemote(IRemote):
    """ Standard remote """
    def __init__(self, device):
        self.device: IDevice = device

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        self._device = device

    def toggle_power(self):
        print('REMOTE: toggling power')

    def volume_down(self):
        print('REMOTE: decreasing volume')

    def volume_up(self):
        print('REMOTE: increasing volume')

    def channel_down(self):
        print('REMOTE: decreasing channel')

    def channel_up(self):
        print('REMOTE: increasing channel')
