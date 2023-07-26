from machine import Pin, ADC
import utime
 
 
sensor = ADC(Pin(36))
sensor.width(ADC.WIDTH_10BIT) 
 
while True:
    
    lectura =  float(sensor.read())
    print(lectura)
    utime.sleep_ms(50)
    