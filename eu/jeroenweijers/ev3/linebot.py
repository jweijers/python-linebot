from eu.jeroenweijers.ev3.behaviour.findRedBehaviour import FindRedBehaviour
from eu.jeroenweijers.ev3.behaviour.backOffBehaviour import BackOffBehaviour
from eu.jeroenweijers.ev3.behaviour.driveForwardBehaviour import DriveForwardBehaviour
from eu.jeroenweijers.ev3.behaviour.subsumption import Controller
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                 InfraredSensor)
from pybricks.parameters import Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font
import logging as log


class LineBot:
    
    def __init__(self, leftMotorPort, rightMotorPort, colorSensorPort, irSensorPort) -> None:
        self.leftMotor = Motor(leftMotorPort, positive_direction=Direction.COUNTERCLOCKWISE)
        self.rightMotor = Motor(rightMotorPort, positive_direction=Direction.COUNTERCLOCKWISE)
        self.colorSensor = ColorSensor(colorSensorPort)
        self.irSensor = InfraredSensor(irSensorPort)
        self.robot = DriveBase(self.leftMotor, self.rightMotor, wheel_diameter=43, axle_track=165)
        self.ev3 = EV3Brick()
        self.angle = 0

    def start(self):
        log.debug("Starting robot")

        self.ev3.screen.clear()
        self.ev3.screen.set_font(Font(size=24, monospace=True, lang='en'))
        self.ev3.screen.draw_text(30, 40, "Hello lego!")
        # Wait until any Brick Button is pressed.
        while not any(self.ev3.buttons.pressed()):
            wait(10)
        wait(1000)
        controller = Controller(True)
        controller.add(BackOffBehaviour(self.robot, self.irSensor))
        controller.add(FindRedBehaviour(self.robot, self.colorSensor))
        controller.add(DriveForwardBehaviour(self.robot))
        controller.start(True)
        
        while not any(self.ev3.buttons.pressed()):
            wait(10)
        controller.stop()
        self.ev3.speaker.beep()
        log.debug("Shutting down")
