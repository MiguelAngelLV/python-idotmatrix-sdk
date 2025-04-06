"""IDotMatrix Image Control Class."""
# pylint: disable=W0246

from bleak import BleakClient

from .idotmatrix_base import IDotMatrixBase


class IDotMatrixImage(IDotMatrixBase):
    """Class to control the image mode of the IDotMatrix."""

    def __init__(self, connection: BleakClient):
        """Initialize the image mode control class."""
        super().__init__(connection)

    async def set_image_mode(self, mode: int):
        """Set the image mode for the LED matrix."""
        data = bytearray([5, 0, 4, 1, mode])
        await self.write(data)
