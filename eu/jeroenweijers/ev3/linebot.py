from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font, SoundFile, ImageFile
import logging

def start():
    logging.debug("Starting robot")
    # Create your objects here.
    ev3 = EV3Brick()
    ev3.screen.clear()
    ev3.screen.set_font(Font(size=24, monospace=True, lang='en'))
    ev3.screen.draw_text(30, 40, "Hello lego!")
    # Wait until any Brick Button is pressed.
    while not any(ev3.buttons.pressed()):
        wait(10)
    
    ev3.speaker.beep()
    logging.debug("Shutting down")