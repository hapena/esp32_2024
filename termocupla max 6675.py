from machine import Pin
import utime 
from MAX6675 import MAX6675

so = Pin(15, Pin.IN)
sck = Pin(13, Pin.OUT)
cs = Pin(14, Pin.OUT)

max = MAX6675(sck, cs , so)


while True:
   
    temperatura= max.read()
    print(temperatura)     

    utime.sleep(1)