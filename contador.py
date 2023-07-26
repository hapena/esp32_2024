from machine import Pin
import utime


push = Pin(4,Pin.IN,Pin.PULL_DOWN)  

contador=0

while True:
    
    
    estado = push.value()
    print(estado)
    if estado == 1:
        contador = contador  + 1
        print(contador)
    
    utime.sleep(2)
             

        



    
    