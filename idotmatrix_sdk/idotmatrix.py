"""IDotMatrix SDK for controlling IDotMatrix devices."""
# pylint: disable=W0246

from dataclasses import dataclass

from bleak import BleakScanner, AdvertisementData, BleakClient

from .idotmatrix_countdown import IDotMatrixCountDown
from .idotmatrix_effects import IDotMatrixEffects
from .idotmatrix_image import IDotMatrixImage
from .idotmatrix_screen import IDotMatrixScreen
from .idotmatrix_time import IDotMatrixTime

DEVICES_NAMES = "IDM-"


@dataclass
class IDMDevice:
    """Class to represent an IDotMatrix device."""

    name: str
    address: str


class IDotMatrix(
    IDotMatrixScreen,
    IDotMatrixTime,
    IDotMatrixCountDown,
    IDotMatrixEffects,
    IDotMatrixImage,
):
    """Class to control the IDotMatrix device."""

    def __init__(self, mac: str):
        """Initialize the IDotMatrix class."""
        self._mac = mac
        self._connection = BleakClient(self._mac)
        super().__init__(self._connection)

    async def connect(self):
        """Connect to the device."""
        await self._connection.connect()

    async def disconnect(self):
        """Disconnect from the device."""
        if self.is_connected:
            await self._connection.disconnect()

    @property
    def is_connected(self):
        """Check if the device is connected."""
        return self._connection and self._connection.is_connected

    @staticmethod
    async def search_devices() -> list[IDMDevice]:
        """Search for IDotMatrix devices."""
        response = await BleakScanner.discover(return_adv=True)
        devices = []
        for _, (device, advertisement) in response.items():
            if (
                isinstance(advertisement, AdvertisementData)
                and advertisement.local_name
                and advertisement.local_name.startswith(DEVICES_NAMES)
            ):
                devices.append(IDMDevice(advertisement.local_name, device.address))

        return devices
