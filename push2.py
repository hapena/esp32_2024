from machine import Pin
from utime import sleep_ms


sensor = Pin(21, Pin.IN, Pin.PULL_DOWN)  

contador = 0

while True:
    
    
    estado = sensor.value()
    #print(estado)
    sleep_ms(200)
    
    if estado == 1:
        display(0,0,1)
    
    else:
        display(0,1,0)
        
    
    
    