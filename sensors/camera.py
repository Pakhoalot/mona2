#!/usr/bin/env python
# -*- coding: utf-8 -*-

'camera post'


__author__ = 'PakhoLeung'

import time

import picamera
import requests
import config
from sensors import sensor

class Camera(sensor.Sensor):

    # 初始化摄像头
    def __init__(self, user_id, device_id, sensor_id):
        super().__init__()
        self.user_id = user_id
        self.device_id = device_id
        self.sensor_id = sensor_id

    # 上传照片
    def upload(self, file_path):
        data = {
            'user_id': self.user_id,
            'device_id': self.device_id,
            'sensor_id': self.sensor_id,
        }
        files = {
            'img': open(file_path, 'rb')
        }
        url = config.UPLOAD_IMG_URL
        response = requests.post(url, data=data, files=files)
        print('uploading ' + file_path + ' to ' + url)

    def collect(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (400, 300)
            camera.start_preview()
            # 摄像头预热
            print('camera prepare')
            time.sleep(config.PREVIEW_TIME)
            t = str(int(time.time()))
            file_path = config.IMG_PATH + t + '.jpg'
            camera.capture(file_path)
            print('capture ' + file_path)
            return file_path

    # def upload end.

    def loop(self):
        while self.isRun:
            file_path = self.collect()
            self.upload(file_path=file_path)
            time.sleep(config.CAPTURE_PERIOD)


if __name__ == '__main__':
    Camera(user_id=1, device_id=1, sensor_id=2).loop()

