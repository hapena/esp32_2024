import esp32
from machine import Pin
import utime




while True:
    
    temp = esp32.raw_temperature()
    hall = esp32.hall_sensor() 
    
    temp_cen =  ((temp - 32)*5)/9
    print(temp, hall, temp_cen)
    utime.sleep_ms(100)
