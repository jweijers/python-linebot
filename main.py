#!/usr/bin/env pybricks-micropython
import logging

from pybricks.parameters import Port
from eu.jeroenweijers.ev3.linebot import LineBot


def main():
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    logging.info('Started')
    robot = LineBot(Port.C, Port.B, Port.S3, Port.S4)
    robot.start()
    logging.info('Finished')

if __name__ == '__main__':
    main()


