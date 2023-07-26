from machine import Pin
import utime
import _thread


push = Pin(13, Pin.IN, Pin.PULL_DOWN)# conectado al positivo  (0)  oprimir (1)
uno = Pin(2, Pin.OUT)
dos = Pin(4, Pin.OUT)
tres = Pin(14, Pin.OUT)

def nucleo_dos():
    
    while True:
        dos.value(1)
        utime.sleep(0.05)
        dos.value(0)
        utime.sleep(0.05)

_thread.start_new_thread(nucleo_dos, () )

while True:
    
    estado = push.value()
    print(estado)
    utime.sleep(0.05)
    
    if estado == 0:
        uno.value(1)
    else:
        uno.value(0)    
     
if __name__==("__main__"):
    main()
