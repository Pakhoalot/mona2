#!/usr/bin/env python

# -*- coding:utf-8 -*-

''

__author__ = 'PakhoLeung'

# from sensors import sensor

import time
import sensor
import threading
import RPi.GPIO as GPIO


class Servo(sensor.Sensor):
    __channel = None
    __pwm = None
    __freq = None #frequent
    __dc = None #duty cycle

    def __init__(self, channel: int):
        super().__init__()
        freq = 50
        self.__channel = channel
        GPIO.setup(self.__channel, GPIO.OUT, initial=False)
        self.__freq = freq
        self.__pwm = GPIO.PWM(self.__channel, self.__freq)

    def stop(self):
        self.__pwm.stop()

    def getChannel(self):
        return self.__channel

    def start(self, dc):
        self.__dc = dc
        self.__pwm.start(self.__dc)

    def changeFrequency(self, freq):
        self.__freq = freq
        self.__pwm.ChangeFrequency(self.__freq)

    def changeDC(self, dc):
        self.__dc = dc
        self.__pwm.ChangeDutyCycle(self.__dc)

    def spin(self, angle):
        # 该函数传入一个角度制角度，为舵机旋转一定角度
        # 这是一个耗时函数，请不要在主函数使用该函数
        if angle<0 or angle>180:
            raise ValueError("Angle is out of Bound.")
        if threading.current_thread() == threading._main_thread:
            raise threading.ThreadError("spin is a time-consuming job. Can't run in mainThread.")
        self.__dc = (angle / (180 - 0)) * (12.5 - 2.5) + 2.5
        self.changeDC(self.__dc)
        time.sleep(0.5)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    servo = Servo(7, 50)
    servo.start(0)

    servo.spin(170)

    servo.stop()
    GPIO.cleanup()
