from machine import Pin
import utime

rojo = Pin(15,Pin.OUT)
amarillo = Pin(2,Pin.OUT)
verde = Pin(4,Pin.OUT)
push = Pin(13,Pin.IN,Pin.PULL_DOWN)  #  siempre en estado cero ... puls a VCC


leds = [rojo, amarillo, verde, amarillo]


def semaforo():
    
    for i in leds:
        i.value(1)
        utime.sleep(1)
        i.value(0)
        utime.sleep(1)

def pausa():
    rojo.value(1)
    utime.sleep(10)
 
while True:
        
        estado = push.value()
        print(estado)
        if estado==1:
            pausa()
            
        else:            
            semaforo()
              
if __name__==("__main__"):
    main()   