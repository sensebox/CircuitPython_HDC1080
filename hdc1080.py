# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 sensebox
#
# SPDX-License-Identifier: MIT
"""
`hdc1080`
================================================================================


.. todo:: Describe what the library does.


* Author(s): sensebox

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/sensebox/CircuitPython_HDC1080.git"

import time
from adafruit_bus_device.i2c_device import I2CDevice

# HDC1080 Default I2C Address
HDC1080_I2C_ADDR = 0x40

# HDC1080 Registers
HDC1080_TEMP_REG = 0x00
HDC1080_HUMIDITY_REG = 0x01
HDC1080_CONFIG_REG = 0x02


class HDC1080:
    """Library for the HDC1080 Temperature and Humidity Sensor.

    :param ~busio.I2C i2c_bus: The I2C bus the HDC1080 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x40`

    **Quickstart: Importing and using the HDC1080**

        Here is an example of using the :class:`HDC1080` class.
        First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            from hdc1080.basic import HDC1080

        Once this is done you can define your `board.I2C` object and define your sensor object

        .. code-block:: python

            i2c = board.I2C()   # uses board.SCL and board.SDA
            hdc = HDC1080(i2c)

        Now you have access to the :attr:`temperature` and :attr:`humidity` attributes.

        .. code-block:: python

            temperature = hdc.temperature
            humidity = hdc.humidity

    """

    def __init__(self, i2c, address=HDC1080_I2C_ADDR):
        self.i2c_device = I2CDevice(i2c, address)
        self._buffer = bytearray(2)
        # self.reset() // Reset is not causing error

    def reset(self):
        """
        reset the sensor
        """
        with self.i2c_device as i2c:
            # Writing to the configuration register to reset
            i2c.write(bytes([0x0, 0x0]))

    @property
    def temperature(self):
        """
        read the temperature from the sensor and return it
        """
        with self.i2c_device as i2c:
            i2c.write(bytes([HDC1080_TEMP_REG]))
            time.sleep(0.0625)  # Temperature conversion time
            i2c.readinto(self._buffer)
            raw_temp = (self._buffer[0] << 8) | self._buffer[1]
            return (raw_temp / 65536.0) * 165.0 - 40.0

    @property
    def humidity(self):
        """
        read the humidity from the sensor and return it
        """
        with self.i2c_device as i2c:
            i2c.write(bytes([HDC1080_HUMIDITY_REG]))
            time.sleep(0.0625)  # Humidity conversion time
            i2c.readinto(self._buffer)
            raw_humidity = (self._buffer[0] << 8) | self._buffer[1]
            return (raw_humidity / 65536.0) * 100.0

    @property
    def serial_number(self):
        """
        read the serial_number from the sensor and return it
        """
        with self.i2c_device as i2c:
            i2c.write(b"\xfc\x0d")  # Reading serial number register
            time.sleep(0.1)  # Wait for serial number to be ready
            i2c.readinto(self._buffer)
            return (
                (self._buffer[0] << 24)
                | (self._buffer[1] << 16)
                | (self._buffer[2] << 8)
                | self._buffer[3]
            )

    @property
    def firmware_version(self):
        """
        read the firmware_version from the sensor and return it
        """
        with self.i2c_device as i2c:
            i2c.write(b"\x2d\x00")  # Reading firmware version register
            time.sleep(0.1)  # Wait for firmware version to be ready
            i2c.readinto(self._buffer)
            return (self._buffer[0] << 8) | self._buffer[1]

    def configure(self, heater=False, mode="sequential", battery_status=False):
        """
        provide sensor configuration options
        """
        config_value = 0x1000 if heater else 0x0000
        if mode == "sequential":
            config_value |= 0x0000
        elif mode == "acquisition":
            config_value |= 0x0100
        else:
            raise ValueError("Invalid mode. Must be 'sequential' or 'acquisition'")
        config_value |= 0x0001 if battery_status else 0x0000

        with self.i2c_device as i2c:
            i2c.write(
                bytes(
                    [
                        HDC1080_CONFIG_REG,
                        (config_value >> 8) & 0xFF,
                        config_value & 0xFF,
                    ]
                )
            )
