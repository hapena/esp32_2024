from machine import Pin
import time

led_a = Pin(8,Pin.OUT)



while True:
        led_a.value(0)
        print("on")
        time.sleep(0.3)
        led_a.value(1)
        print("off")
        time.sleep(0.3)
      
        
        
        
        