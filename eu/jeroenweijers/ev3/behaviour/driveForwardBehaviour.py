from pybricks.robotics import DriveBase
import eu.jeroenweijers.ev3.behaviour.subsumption as sub
import logging as log
from pybricks.tools import wait

class DriveForwardBehaviour(sub.Behavior):

    def __init__(self, robot: DriveBase) -> None:
        self.robot = robot
        self.suppressed = False
    
    def check(self):
        
        return True 

    def action(self):
        log.debug("Power")
        self.suppressed = False
        self.robot.drive(75, 0)
        while not self.suppressed:
            wait(1)
        self.robot.stop()

    def suppress(self):
        log.debug("Suppress forward")
        self.suppressed = True
    

        
