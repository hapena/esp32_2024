from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep
from dht import DHT11


sensorDHT= DHT11(Pin(15))

file = open("dato.csv", "w")

ancho = 128
alto = 64
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())

while True:
    
    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    
    # mostrar en pantalla
    oled.text("Temperatura", 0, 0)
    oled.text(str(temp), 0, 10)
    oled.text("Humedad", 0, 20)
    oled.text(str(hum), 0, 30)
    oled.show()
    
    
    file.write(str("T={:02}C H={:02}% \n".format(temp, hum)))
    file.flush()
               
    print("T={:02d}C H={:02d}%".format(temp, hum))
    
    
    
    
