#!/usr/bin/env python

#-*- coding:utf-8 -*-

'main'

__author__ = 'PakhoLeung'

import time
import threading
import sensors.camera as C
import sensors.led as L
import RPi.GPIO as GPIO





if __name__ == '__main__':
    try:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        camera = C.Camera(user_id=1, device_id=1, sensor_id=2)
        led1 = L.LED(3)
        led2 = L.LED(5)

        t1 = threading.Thread(target=led1.loop,args=())
        t2 = threading.Thread(target=led2.loop, args=())
        t3 = threading.Thread(target=camera.loop, args=())

        t1.start()
        t2.start()
        t3.start()



    except KeyboardInterrupt:
        camera.stop()
        led1.stop()
        led2.stop()
        t1.join()
        t2.join()
        t3.join()
        print('main ends')
