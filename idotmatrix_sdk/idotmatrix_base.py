"""IDotMatrix Base Class."""
# pylint: disable=W0246

from asyncio import sleep

from bleak import BleakClient


UUID_WRITE = "0000fa02-0000-1000-8000-00805f9b34fb"
UUID_READ = "0000fa03-0000-1000-8000-00805f9b34fb"


class IDotMatrixBase:
    """Base class for IDotMatrix control classes."""

    def __init__(self, connection: BleakClient):
        """Initialize the base class with a BleakClient connection."""
        self._connection = connection

    async def write(self, data: bytes, response: bool = False):
        """Send data to the device."""
        if not self._connection.is_connected:
            return

        await self._connection.write_gatt_char(UUID_WRITE, data, response)
        await sleep(0.1)

    async def read(self) -> bytes:
        """Read data from the device."""
        if not self._connection.is_connected:
            return bytes()

        data = await self._connection.read_gatt_char(UUID_READ)
        return data
