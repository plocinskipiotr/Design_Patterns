"""
Main loop for bridge example
"""

from standard_remote import StandardRemote
from advanced_remote import AdvancedRemote
from television import TV
from radio import Radio

if __name__ == '__main__':
    RadioInstance = Radio()
    TVInstance = TV()

    StandardRemoteInstance = StandardRemote(RadioInstance)

    StandardRemoteInstance.volume_up()
    StandardRemoteInstance.device.enable()

    StandardRemoteInstance = StandardRemote(TVInstance)

    StandardRemoteInstance.volume_up()
    StandardRemoteInstance.device.enable()

    AdvancedRemoteInstance = AdvancedRemote(RadioInstance)

    AdvancedRemoteInstance.volume_up()
    AdvancedRemoteInstance.device.enable()

    AdvancedRemoteInstance = AdvancedRemote(TVInstance)

    AdvancedRemoteInstance.volume_up()
    AdvancedRemoteInstance.device.enable()

    AdvancedRemoteInstance.mute()
