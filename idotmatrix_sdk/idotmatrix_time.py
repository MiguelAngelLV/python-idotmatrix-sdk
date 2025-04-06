"""IDotMatrixTime class for controlling the time on the IDotMatrix device."""
# pylint: disable=W0246

from datetime import datetime

from bleak import BleakClient

from .idotmatrix_base import IDotMatrixBase
from .idotmatrix_color import IDotMatrixColor


class IDotMatrixTime(IDotMatrixBase):
    """Class for controlling the time on the IDotMatrix device."""

    def __init__(self, connection: BleakClient):
        """Initialize the IDotMatrixTime class."""
        super().__init__(connection)

    async def set_time(self, time: datetime):
        """Set the time for the IDotMatrix device."""
        data = bytearray(
            [
                11,
                0,
                1,
                128,
                time.year % 100,
                time.month,
                time.day,
                time.weekday() + 1,
                time.hour,
                time.minute,
                time.second,
            ]
        )

        await self.write(data)

    async def set_time_mode(
        self, mode: int, show_date: bool, mode24: bool, color: IDotMatrixColor
    ):
        """Set the time mode for the IDotMatrix device."""

        if mode not in range(0, 8):
            raise ValueError(f"Invalid mode ({mode}) value.")

        data: bytearray = bytearray(
            [
                8,
                0,
                6,
                1,
                (mode % 8) | (128 if show_date else 0) | (64 if mode24 else 0),
                color.red,
                color.green,
                color.blue,
            ]
        )
        await self.write(data)
