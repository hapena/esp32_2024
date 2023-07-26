from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from utime import sleep

sensorG = ADC(Pin(36))
sensorG.width(ADC.WIDTH_10BIT)
sensorG.atten(ADC.ATTN_11DB)
file = open("test.txt", "w")

ancho = 128
alto = 64

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())
 
oled.text('Welcome to the', 0, 0)
oled.text('Areandina', 0, 10)
oled.text('Control de Nivel de gas', 0, 20)
oled.show()
sleep(2)
 

 
while True:
    
    
    sleep(2)
    lectura = sensorG.read()
    file.write(str( "Nivel de gas =  {} % ".format(lectura)))
    file.flush()
    oled.fill(0)
    oled.text("Nivel de gas: ",0,10)
    oled.text(str(lectura),0,20)
    oled.show()
    
    print("Nivel de gas: ",lectura)
    sleep(0.25)