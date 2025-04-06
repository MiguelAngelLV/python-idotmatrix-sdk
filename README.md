# I Dot Matrix SDK

I Dot Matrix SDK is a Python library for controlling the I Dot Matrix display. It provides an easy-to-use interface for controlling the display based on [python3-idotmatrix-library](https://github.com/derkalle4/python3-idotmatrix-library)

## Features

- Multiple devices support
- Control the I Dot Matrix display (brightness, turn on/off, etc.)
- Time functionality
- Countdown functionality

## TODO
- Text support
- Image support

## Installation

You can install the package using pip:

```bash
pip install idotmatrix-sdk
```

## Usage

```python
import asyncio
import logging
import datetime

from idotmatrix_sdk import IDotMatrix
from idotmatrix_sdk import IDotMatrixColor

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    async def main():
        devices = await IDotMatrix.search_devices()
        if not devices:
            print("No devices found")
            return

        device = devices[0]
        print(f"Connecting to {device.name} ({device.address})")

        dot_matrix = IDotMatrix(device.address)
        await dot_matrix.connect()

        # Example usage of the IDotMatrix class
        await dot_matrix.set_time(datetime.datetime.now())
        await dot_matrix.turn_on()
        await dot_matrix.set_brightness(100)
        await dot_matrix.set_time_mode(3, True, True, IDotMatrixColor.random_color())

    asyncio.run(main())

```