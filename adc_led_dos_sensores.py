from machine import Pin, ADC
import utime
 
 
sensor_a = ADC(Pin(36))
sensor_b = ADC(Pin(39))
led = Pin(15, Pin.OUT)
 
while True:
    
    lectura_a =  float(sensor_a.read_u16())
    lectura_b =  float(sensor_b.read_u16())
    print(lectura_a)
    print(lectura_b)
    utime.sleep(0.25)
    
    if lectura_a < 2000:
        
        led.value(1)
        
    else:
        
        led.value(0)
    