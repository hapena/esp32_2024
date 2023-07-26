from machine import Pin
import utime

led_a = Pin(15,Pin.OUT)
led_b = Pin(2,Pin.OUT)
push = Pin(4,Pin.IN,Pin.PULL_DOWN)  #  siempre en estado cero ... puls a VCC

while True:
    
        
        estado = push.value()
        print(estado)
        if estado==0:            
            led_a.value(0)
            led_b.value(1)
        else:
            led_a.value(1)
            led_b.value(0)
              
        utime.sleep(0.25)   
 
if __name__==("__main__"):
    main()
    
    
    
    
    
    