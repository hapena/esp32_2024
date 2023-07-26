from machine import Pin, ADC, I2C
import utime
from ssd1306 import SSD1306_I2C

# Indicadores
led_rojo= Pin(15, Pin.OUT)
led_verde = Pin(2, Pin.OUT)

ancho = 128
alto = 64


i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

# calibrar.... de acuerdo a las especificaciones del sensor
sensor = ADC(Pin(39))
sensor.atten(ADC.ATTN_11DB)  # para calibrar de 0 a 3.6v
sensor.width(ADC.WIDTH_12BIT) # establecer resolucion de 12 bits hasta 4096

print(i2c.scan())

while True:
    # sensor
    oled.fill(0)
    lectura =  sensor.read()
    factor_de_conversion = 400/4096
    distancia = factor_de_conversion * lectura
    print("D: ",distancia)
       
    # mostrar en pantalla
    oled.text("Distancia", 0, 0)
    oled.text(str(distancia), 0, 10)
    oled.fill_rect(1 ,30, int(distancia), 30 ,1)
    oled.show()
    utime.sleep_ms(50)
    
    
    # toma de desciciones 
    if distancia < 20:
        
        led_rojo.value(1)
        led_verde.value(0)
        
        
    else:
        led_rojo.value(0)
        led_verde.value(1)
        


