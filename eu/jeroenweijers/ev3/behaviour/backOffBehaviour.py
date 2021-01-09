from pybricks.ev3devices import InfraredSensor
from pybricks.robotics import DriveBase
import eu.jeroenweijers.ev3.behaviour.subsumption as sub
import logging as log
from pybricks.tools import wait

class BackOffBehaviour(sub.Behavior):

    def __init__(self, robot: DriveBase, irSensor: InfraredSensor) -> None:

        self.robot = robot
        self.irSensor = irSensor
        self.suppressed = False
    
    def check(self):
        distance = self.irSensor.distance()
        #log.debug("distance: " + str(distance))
        return distance < 50

    def action(self):
        log.debug("Backing off")
        self.suppressed = False
        self.robot.drive(-100, 0)
        while not self.suppressed and self.check():
            wait(1)
        self.suppress()
        self.robot.stop()

    def suppress(self):
        log.debug("Suppress backoff")
        self.suppressed = True