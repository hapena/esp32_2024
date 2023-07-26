from machine import Pin
import time


led_a = Pin(15,Pin.OUT)
led_b = Pin(2,Pin.OUT)
push = Pin(13,Pin.IN,Pin.PULL_UP)

while True:
        
        estado = push.value()
        print(estado)
        if estado==0:
            led_a.value(0)
            led_b.value(1)
        else:
            
            led_a.value(1)
            led_b.value(0)
              
        time.sleep(0.25)   
    
        
   