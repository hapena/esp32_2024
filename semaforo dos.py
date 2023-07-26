from machine import Pin
import utime


led_rojo = Pin(15,Pin.OUT)
led_amarillo = Pin(2,Pin.OUT)
led_verde = Pin(4,Pin.OUT)



while True:
        led_rojo.value(1)
        led_amarillo.value(0)
        led_verde.value(0)
        print("Rojo")
        utime.sleep(2)
        
        led_rojo.value(0)
        led_amarillo.value(1)
        led_verde.value(0)
        print("Amrillo")
        utime.sleep(2)
        
        led_rojo.value(0)
        led_amarillo.value(0)
        led_verde.value(1)
        print("verde")
        utime.sleep(2)
        
        
        
        