from machine import Pin
import time


led_a = Pin(9,Pin.OUT)
led_b = Pin(8,Pin.OUT)
push = Pin(2,Pin.IN,Pin.PULL_UP)

while True:
        
        estado= push.value()
        print(estado)
        if estado==0:
            print("verde")
            led_a.value(0)
            led_b.value(1)
        else:
            print("Rojo")
            led_a.value(1)
            led_b.value(0)
              
        time.sleep(0.25)   
    
        
   