from machine import Pin
import time

led_a = Pin(5,Pin.OUT)
led_b = Pin(4,Pin.OUT)


while True:
        led_a.value(0)
        led_b.value(1)
        time.sleep(0.3)
        led_a.value(1)
        led_b.value(0)
        time.sleep(0.3)
      
        
        
        
        