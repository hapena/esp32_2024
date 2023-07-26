from machine import Pin, TouchPad
import time
Touch = TouchPad(Pin(4))
led = Pin(2, Pin.OUT) 

while True:
    
    valor= Touch.read()
    print(valor)
    
    if Touch.read()<300:             # si el tiempo se ha agotado y T0 tiene contacto...                            
        led.on()                # ... se enciende el LED
    else:                         # si el tiempo se ha agotado y T0 no tiene contacto...
        led.off()               # ...se apaga el LED
        
        