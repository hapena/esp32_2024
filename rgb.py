from machine import Pin 
from utime import sleep_ms

r = Pin(4, Pin.OUT)
g= Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)


def display(R, G, B):
  

  r.value(R)
  g.value(G)
  b.value(B)
  

while True:
  
  print("iniciando")  
  display(0,0,0)
  sleep_ms(1000)
  display(0,0,1)
  sleep_ms(1000)
  display(0,1,0)
  sleep_ms(1000)
  display(0,1,1)
  sleep_ms(1000)
  display(1,0,0)
  sleep_ms(1000)
  display(1,0,1)
  sleep_ms(1000)
  display(1,1,0)
  sleep_ms(1000)
  display(1,1,1)
  sleep_ms(1000)
 
  