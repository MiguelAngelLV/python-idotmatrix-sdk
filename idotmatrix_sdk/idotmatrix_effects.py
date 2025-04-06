"""IDotMatrix Effects Control Class."""
# pylint: disable=W0246

from bleak import BleakClient

from .idotmatrix_base import IDotMatrixBase
from .idotmatrix_color import IDotMatrixColor


class IDotMatrixEffects(IDotMatrixBase):
    """Class to control the LED matrix effects of the IDotMatrix."""

    def __init__(self, connection: BleakClient):
        """Initialize the LED matrix effects control class."""
        super().__init__(connection)

    async def set_color(self, color: IDotMatrixColor):
        """Set the color of the LED matrix."""
        data = bytearray(
            [
                7,
                0,
                2,
                2,
                color.red,
                color.green,
                color.blue,
            ]
        )
        await self.write(data)
