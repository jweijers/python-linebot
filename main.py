#!/usr/bin/env pybricks-micropython
import logging
import eu.jeroenweijers.ev3.linebot as bot

# This program requires LEGO EV3 MicroPython v2.0 or higher.


def main():
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    logging.info('Started')
    bot.start()
    logging.info('Finished')

if __name__ == '__main__':
    main()


