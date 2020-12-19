#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import logging

# This program requires LEGO EV3 MicroPython v2.0 or higher.


def main():
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    logging.info('Started')
    linebot()
    logging.info('Finished')


def linebot():
    logging.debug("Starting robot")
    # Create your objects here.
    ev3 = EV3Brick()

    # Write your program here.
    ev3.speaker.beep()
    logging.debug("Shutting down")


if __name__ == '__main__':
    main()


