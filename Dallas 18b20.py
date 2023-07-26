from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
 
ds = DS18X20(OneWire(Pin(4)))
sensor_id = ds.scan()[0]  
 
while True:
    ds.convert_temp()    
    tem= ds.read_temp(sensor_id)
    print(tem, " °C")
    sleep_ms(500)  
    