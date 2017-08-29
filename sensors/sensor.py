#!/usr/bin/env python

#-*- coding:utf-8 -*-

'sensor class'

__author__ = 'PakhoLeung'

import threading,time

class Sensor:

    isRun = True

    def stop(self):
        print(self.__str__()+' ends')
        self.isRun = False

    def start(self):
        print(self.__str__()+' start')

    def __init__(self):
        super().__init__()

    def upload(self):
        print(threading.current_thread().getName() + ' is uploading')
        pass

    def collect(self):
        print(threading.current_thread().getName() + ' is collecting')
        pass

    def loop(self):
        pass