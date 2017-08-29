#!/usr/bin/env python

#-*- coding:utf-8 -*-

''
import time

__author__ = 'PakhoLeung'

# from sensors import sensor
import sensor
import RPi.GPIO as GPIO

class HumanDetector(sensor.Sensor):

    __channel = None

    def __init__(self, channel:int):
        super().__init__()
        self.__channel = channel
        GPIO.setup(self.__channel, GPIO.IN)


    def detect(self):
        return GPIO.input(self.__channel)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    hd = HumanDetector(11)
    while True:
        if hd.detect():
            print("Someone's here")
        else :
            print("Noone here")
        time.sleep(2)

    GPIO.cleanup()
