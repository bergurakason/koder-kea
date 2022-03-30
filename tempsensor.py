import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

def tempsensor():
    temperature = sensor.get_temperature()
    return temperature   