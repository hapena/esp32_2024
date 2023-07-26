from machine import SoftI2C, Pin
import ssd1306

i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) # pines I2C
oled = ssd1306.SSD1306_I2C(128,64,i2c)
oled.fill(0)
oled.text("Hola Mundo!",0,0)   
oled.show()
    

