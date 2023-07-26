from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

sensor = ADC(Pin(36))
ancho = 128
alto = 64

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())
 
oled.text('Welcome to the', 0, 0)
oled.text('Areandina', 0, 10)
oled.text('Display Demo', 0, 20)
oled.show()
time.sleep(4)
 
oled.fill(1)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()
 
while True:
    
    
    val = int((sensor.read_u16())/500)
    oled.fill_rect(1,15,val,25,1)
    oled.show()
    oled.fill_rect(1,15,val,25,0)
    time.sleep(0.25) 