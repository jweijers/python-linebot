from pybricks.ev3devices import ColorSensor
from pybricks.robotics import DriveBase
import eu.jeroenweijers.ev3.behaviour.subsumption as sub
from pybricks.parameters import Port, Stop, Direction, Button, Color
import logging as log
from pybricks.tools import wait

class FindRedBehaviour(sub.Behavior):

    def __init__(self, robot: DriveBase, colorSensor: ColorSensor) -> None:
        self.robot = robot
        self.colorSensor = colorSensor
        self.suppressed = False
    
    def check(self):
        return self.continueSearch() 

    def continueSearch(self) -> bool:
        color = self.colorSensor.color()
        return color != Color.RED


    def action(self):
        log.debug("Find red!")
        self.suppressed = False
        rotation = 10
        speed = 20
        dir = 1
        while not self.suppressed and self.continueSearch():
            self.robot.reset()
            self.robot.drive(0, dir * speed)
            while dir * self.robot.angle() < rotation:
                wait(1)
                if self.suppressed or not self.continueSearch():
                    self.robot.stop()
                    self.suppress()
                    return  
            rotation = rotation * 1.5
            dir = dir * -1
        self.suppress()
        self.robot.stop()

    def suppress(self):
        log.debug("Suppress find red")
        self.suppressed = True
    