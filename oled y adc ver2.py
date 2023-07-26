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
    oled.fill(0)
    conversion_factor = 3.3 / (65535)
    val= int(sensor.read_u16())
    voltaje = float (sensor.read_u16()*conversion_factor)
    oled.text("Lectura",0,10)
    oled.text(str(val),0,20)
    oled.text("Voltaje",0,30)                
    oled.text(str(voltaje),0,40)   
    oled.show()
    
    print("Voltaje =", voltaje)
    time.sleep(0.25)