from machine import Pin
from utime import sleep

rojo = Pin(15, Pin.OUT)
amarillo = Pin(2, Pin.OUT)
verde = Pin(4, Pin.OUT)

while True:
    
    rojo.on()
    amarillo.off()
    verde.off()
    sleep(0.3)
    rojo.off()
    amarillo.on()
    verde.off()
    sleep(0.3)
    rojo.off()
    amarillo.off()
    verde.on()
    sleep(0.3)
    



