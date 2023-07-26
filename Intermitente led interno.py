from machine import Pin
import utime


led = Pin(13,Pin.OUT)
while True:
        led.value(1)
        print("led on")
        utime.sleep(0.5)
        led.value(0)
        print("led off")
        utime.sleep(0.5)
        
        
        
        