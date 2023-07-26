from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
from utime import sleep

sensorDHT = DHT11(Pin(15))
file = open("otro.csv", "w")

ancho = 128
alto = 64

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())
 
oled.text('Welcome to the', 0, 0)
oled.text('Areandina', 0, 10)
oled.text('Control de Temperatura', 0, 20)
oled.show()
sleep(2)
 

 
while True:
    
    sleep(2)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    kelvin = temp + 273
    file.write(str("T={:02d} ºC, H={:02d} %  K= {:02d} k   ".format(temp, hum, kelvin) ))
    file.flush()
    oled.fill(0)
    oled.text("Temperatura:",0,10)
    oled.text(str(temp),100,10)
    oled.text("Humedad:",0,20)                
    oled.text(str(hum),100,20)
    oled.text("Kelvin:",0,30)                
    oled.text(str(kelvin),100,30) 
    oled.show()
    
    print("T={:02d} ºC, H={:02d} %  K= {:02d} k".format(temp, hum, kelvin))
    sleep(0.25)