from machine import Pin, ADC
import utime
 
sensor = ADC(Pin(36))
 
while True:
    conversion_factor = 3.3 / (65535)
    lectura = int (sensor.read_u16())
    voltaje = float (sensor.read_u16()*conversion_factor)
    print("lectura:", lectura)
    print("voltaje:", voltaje)
    utime.sleep(0.25)
   