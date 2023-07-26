from machine import Pin
import utime

led_uno = Pin(32, Pin.OUT)
led_dos = Pin(33, Pin.OUT)
led_tres = Pin(25, Pin.OUT)
led_cuatro = Pin(26, Pin.OUT)

def leds(a,b,c,d):
    led_uno.value(a)
    led_dos.value(b)
    led_tres.value(c)
    led_cuatro.value(d)

while True:
    
    leds(0,0,0,0)
    utime.sleep(0.1)
    leds(0,0,0,1)
    utime.sleep(0.1)
    leds(0,0,1,0)
    utime.sleep(0.1)
    leds(0,1,0,0)
    utime.sleep(0.1)
    leds(1,0,0,0)
    utime.sleep(0.1)
    
    
if __name__==("__main__"):
    main()
   
