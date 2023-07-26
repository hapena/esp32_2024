from machine import Pin, ADC
import utime
 
sensor = ADC(Pin(36))
 
while True:
    #conversion_factor = 3.3 / (65535)
    #voltaje = float (sensor.read_u16()*conversion_factor)
    lectura =  float (sensor.read_u16())
    #print("voltaje:", voltaje)
    print(lectura)
    utime.sleep(0.25)
    #print("hola")