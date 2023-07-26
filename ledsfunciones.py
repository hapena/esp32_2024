from machine import Pin
import utime

cero = Pin(15, Pin.OUT)
uno = Pin(2, Pin.OUT)
dos = Pin(4, Pin.OUT)
tres = Pin(16, Pin.OUT)
cuatro = Pin(17, Pin.OUT)
cinco = Pin(5, Pin.OUT)
seis = Pin(18, Pin.OUT)
siete = Pin(19, Pin.OUT)

def leds(a,b,c,d,e,f,g,h):
    
    cero.value(a)
    uno.value(b)
    dos.value(c)
    tres.value(d)
    cuatro.value(e)
    cinco.value(f)
    seis.value(g)
    siete.value(h)       
 
while True:
    leds(0,0,0,0,0,0,0,0)
    utime.sleep(0.1)
    leds(0,0,0,0,0,0,0,1)
    utime.sleep(0.1)
    leds(0,0,0,0,0,0,1,1)
    utime.sleep(0.1)
    leds(0,0,0,0,0,1,1,1)
    utime.sleep(0.1)
    leds(0,0,0,0,1,1,1,1)
    utime.sleep(0.1)
    leds(0,0,0,1,1,1,1,1)
    utime.sleep(0.1)
    leds(0,0,1,1,1,1,1,1)
    utime.sleep(0.1)
    leds(0,1,1,1,1,1,1,1)
    utime.sleep(0.1)
    leds(1,1,1,1,1,1,1,1)
    utime.sleep(0.1)
    
  

if __name__==("__main__"):
    main()