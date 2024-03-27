# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 sensebox
#
# SPDX-License-Identifier: Unlicense

import board
import time
from hdc1080 import HDC1080
import digitalio

# IO Enable Pin (only needed for senseBox MCU-S2)
io_enable_pin = digitalio.DigitalInOut(board.IO_POWER)
io_enable_pin.direction = digitalio.Direction.OUTPUT
io_enable_pin.value = False

# Initialize I2C bus
i2c = board.I2C()

# Initialize HDC1080 sensor
sensor = HDC1080(i2c)

while True:
    temperature = sensor.temperature
    humidity = sensor.humidity

    print("Temperature: {:.2f} °C".format(temperature))
    print("Humidity: {:.2f} %".format(humidity))

    time.sleep(2)  # Wait for 2 seconds before next reading
    

