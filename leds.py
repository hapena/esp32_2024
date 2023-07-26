from machine import Pin
from utime import sleep_ms
import _thread


a = Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(5, Pin.OUT)
e = Pin(18, Pin.OUT)
f = Pin(19, Pin.OUT)
g = Pin(21, Pin.OUT)
h = Pin(22, Pin.OUT)

leds = [a, b, c, d, e, f, g, h]

def nuevo():
    
    while True:
            
        for bombillo in leds[0:4:1]:
        
            bombillo.on()
            sleep_ms(500)
            bombillo.off()
            sleep_ms(500)
            
_thread.start_new_thread(nuevo, ())
            

while True:
    
    for bombillo in leds[4:8:1]:
        
        bombillo.on()
        sleep_ms(50)
        bombillo.off()
        sleep_ms(50)
        
    
        
        
    
    
    
    