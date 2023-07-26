from machine import Pin
import time

push = Pin(2,Pin.IN,Pin.PULL_UP)

while True:
        
        estado= push.value()
        print(estado)
        time.sleep(0.25)   
    
        
   