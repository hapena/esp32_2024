from machine import Pin
import time

led_a = Pin(4,Pin.OUT)



while True:
        
        led_a.value(0)
        print("0ff")
        time.sleep(0.5)
        led_a.value(1)
        print("on")
        time.sleep(0.5)