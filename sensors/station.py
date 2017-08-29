

'camera post'

__author__ = 'PakhoLeung'

# http://shumeipai.nxez.com/2017/07/05/learning-people-in-space-indicator.html


import requests
from gpiozero import LED
from time import sleep
from sensors import sensor

class Station(sensor.Sensor):


    def __init__(self):
        super().__init__()

    def getSpaceNum(self):
        # url = "http://api.open-notify.org/astros.json"
        # r = requests.get(url)
        # j = r.json()
        # n = j['number']
    
        n = 5
        return n

    def showNum(self,num,led):
        for i in range(1,num):
            led.on()
            sleep(0.2)
            led.off()
            sleep(0.2)

    def loop(self):
        led = LED(2)
        led.off()
        while True:
            num = self.getSpaceNum()
            self.showNum(num,led)
            sleep(30)

if __name__ == '__main__':
    Station().start()