HDC1080
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/sensebox/CircuitPython_HDC1080/workflows/Build%20CI/badge.svg
    :target: https://github.com/sensebox/CircuitPython_HDC1080/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black


Libray for the HDC1080 temperature and humidity sensor.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!


On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-hdc1080/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-hdc1080

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-hdc1080

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-hdc1080

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install hdc1080

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    import time
    import board
    import digitalio
    from hdc1080 import HDC1080

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


Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-hdc1080.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/sensebox/CircuitPython_HDC1080/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
