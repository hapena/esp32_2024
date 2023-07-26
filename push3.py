from machine import Pin
from utime import sleep_ms

sensor = Pin(21, Pin.IN, Pin.PULL_DOWN)  

r = Pin(4, Pin.OUT)
g= Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)


def display(R, G, B):

  r.value(R)
  g.value(G)
  b.value(B)

while True:
    
    
    estado = sensor.value()
    #print(estado)
    sleep_ms(50)
    
    if estado == 1:           
          
        display(0,0,1)
    
    else:
        display(1,0,0)
        