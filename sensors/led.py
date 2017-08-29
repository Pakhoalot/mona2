#!/usr/bin/env python

#-*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'
import RPi.GPIO as GPIO
#import config
import time
from sensors import sensor

class LED(sensor.Sensor):

    __channel = None
    __OFF = GPIO.LOW
    __ON = GPIO.HIGH

    def __init__(self, channel) -> None:
        self.__channel = channel
        GPIO.setup(self.channel, GPIO.OUT)
        self.setState(self.__OFF)

    def setState(self, state):
        GPIO.output(self.channel, state)

    def getChannel(self):
        return self.__channel

    def loop(self):
        while self.isRun:
            self.setState(self.__ON)
            time.sleep(2)
            self.setState(self.__OFF)
            time.sleep(2)

        GPIO.cleanup()

if __name__ == '__main__':
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    try:
        LED(3).loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
