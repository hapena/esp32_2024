from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import framebuf

ancho = 128
alto = 64

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)


def buscar_icono(ruta):
    dibujo= open(ruta, "rb")  # Abrir en modo lectura de bist
    dibujo.readline() # metodo para ubicarse en la primera linea de los bits
    xy = dibujo.readline() # ubicarnos en la segunda linea
    x = int(xy.split()[0])  # split  devuelve una lista de los elementos de la variable solo 2 elemetos
    y = int(xy.split()[1])
    icono = bytearray(dibujo.read())  # guardar en matriz de bites
    dibujo.close()
    return framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)# Datos y tamaño de la imagen.

while True: 
    oled.blit(buscar_icono("dibujos/ejemplo.pbm"), 0, 0) # ruta y sitio de ubicación
    oled.show()  #mostrar
    time.sleep(3)
    oled.blit(buscar_icono("dibujos/ejemplo2.pbm"), 0, 0) # ruta y sitio de ubicación
    oled.show()
    time.sleep(3)






