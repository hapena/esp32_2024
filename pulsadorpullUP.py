from machine import Pin
import utime

push = Pin(15, Pin.IN, Pin.PULL_UP) # pulsador conectado a GND
led =  Pin(4, Pin.OUT)

while True:
    
    estado = push.value()
    #print(estado)
    utime.sleep_ms(50)
    
    if estado == 0:
        led.value(1)
        print("alarma")
        
    else:
        led.value(0)
        print("ok")
    
    
    