"""IDotMatrix countdown timer control class."""
# pylint: disable=W0246

from bleak import BleakClient

from .idotmatrix_base import IDotMatrixBase


class IDotMatrixCountDown(IDotMatrixBase):
    """Class to control the countdown timer of the IDotMatrix."""

    def __init__(self, connection: BleakClient):
        """Initialize the countdown timer control class."""
        super().__init__(connection)

    async def start_countdown(self, minutes: int, seconds: int):
        """Start the countdown timer for the specified number of minutes and seconds."""
        if minutes not in range(0, 256):
            raise ValueError(f"Invalid minutes ({minutes}) argument.")

        if seconds not in range(0, 60):
            raise ValueError(f"Invalid seconds ({seconds}) argument.")

        data = bytearray(
            [
                7,
                0,
                8,
                128,
                1,
                minutes,
                seconds,
            ]
        )
        await self.write(data)

    async def pause_countdown(self):
        """Pause the countdown timer."""
        data = bytearray(
            [
                7,
                0,
                8,
                128,
                2,
                0,
                0,
            ]
        )
        await self.write(data)

    async def resume_countdown(self):
        """Resume the countdown timer."""
        data = bytearray(
            [
                7,
                0,
                8,
                128,
                3,
                0,
                0,
            ]
        )
        await self.write(data)

    async def stop_countdown(self):
        """Stop the countdown timer."""
        data = bytearray(
            [
                7,
                0,
                8,
                128,
                0,
                0,
                0,
            ]
        )
        await self.write(data)
