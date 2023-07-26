from machine import I2C, Pin
from utime import sleep, sleep_ms
from bmp280 import BMP280

bus = I2C(0, sda=Pin(21), scl=Pin(22))
bmp = BMP280(bus)

while True:
    print(bmp.temperature)
    print(bmp.pressure)
    sleep_ms(50)
    
    