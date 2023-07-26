
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
from utime import sleep

ancho = 128
alto = 64

sensorDHT = DHT11(Pin(15))
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())


while True:
 
    sensorDHT.measure()
    tem = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    oled.fill(0)
    oled.text("Temperatura", 0 , 0) # columna ---- fila
    oled.text(str(tem), 0 ,10)
    oled.text("Humedad", 0, 20)
    oled.text(str(hum), 0, 30)
    oled.show()
    print("T={:02.1f}°c , H={:02.1f}% ".format(tem, hum))
    sleep(2)
    
    

