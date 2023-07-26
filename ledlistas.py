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

leds= [cero, uno, dos, tres, cuatro, cinco, seis, siete]

def derecha():
    for i in leds[::1]:
        i.value(1)
        utime.sleep_ms(30)
        i.value(0)
        utime.sleep_ms(30)
        
def izquierda():
    for i in leds[::-1]:
        i.value(1)
        utime.sleep_ms(30)
        i.value(0)
        utime.sleep_ms(30)
    
    
while True:
    derecha()
    utime.sleep(0.1)
    izquierda()
    utime.sleep(0.1)
    
  

if __name__==("__main__"):
    main()