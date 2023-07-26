from machine import Pin
import utime

push = Pin(21, Pin.IN, Pin.PULL_UP) # conectado al negativo (1)  oprimir (0)
uno = Pin(2, Pin.OUT)

while True:
    
    estado = push.value()
    print(estado)
    utime.sleep(0.05)
    
    '''if estado == 0:
        uno.value(1)
    else:
        uno.value(0) '''   
     
if __name__==("__main__"):
    main()