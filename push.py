from machine import Pin
from utime import  sleep_ms 

sensor = Pin(21, Pin.IN, Pin.PULL_UP)


while True:
    
    estado = sensor.value()
    print(estado)
    sleep_ms(200)
    
    