from machine import Pin, ADC
import utime
 
 
sensor = ADC(Pin(36))
led = Pin(15, Pin.OUT)
 
while True:
    
    lectura =  float(sensor.read_u16())
    print(lectura)
    utime.sleep(0.25)
    
    if lectura < 20000:
        led.value(1)
        
    else:
        
        led.value(0)
    