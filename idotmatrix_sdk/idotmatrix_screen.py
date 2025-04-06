"""IDotMatrix screen control class."""
# pylint: disable=W0246

from bleak import BleakClient

from .idotmatrix_base import IDotMatrixBase


class IDotMatrixScreen(IDotMatrixBase):
    """Class to control the screen of the IDotMatrix."""

    def __init__(self, connection: BleakClient):
        """Initialize the screen control class."""
        super().__init__(connection)

    async def turn_off(self):
        """Turn off the IDotMatrix screen."""
        data = bytearray([5, 0, 7, 1, 0])
        await self.write(data)

    async def turn_on(self):
        """Turn on the IDotMatrix screen."""
        data = bytearray([5, 0, 7, 1, 1])
        await self.write(data)

    async def flip(self, flip: bool):
        """Flip the IDotMatrix screen."""
        data = bytearray([5, 0, 6, 128, 1 if flip else 0])
        await self.write(data)

    async def set_brightness(self, brightness: int):
        """Set the brightness of the IDotMatrix screen. Minimum is 5, maximum is 100."""
        if brightness not in range(5, 101):
            raise ValueError(f"Invalid brightness ({brightness}) argument.")

        brightness = max(5, min(100, brightness))
        data = bytearray([5, 0, 4, 128, brightness])
        await self.write(data)
