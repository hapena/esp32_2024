from machine import Pin, ADC, PWM, I2C
from utime import sleep, sleep_ms
from sh1106 import SH1106_I2C
import framebuf

alto = 64
ancho = 128

i2c=I2C(0, scl=Pin(5), sda=Pin(4))
oled = SH1106_I2C(ancho, alto, i2c)


print(i2c.scan(), "conectada")

def buscar_icono(ruta):
    dibujo= open(ruta, "rb")  # Abrir en modo lectura de bits
    dibujo.readline() # metodo para ubicarse en la primera linea de los bits
    xy = dibujo.readline() # ubicarnos en la segunda linea
    x = int(xy.split()[0])  # split  devuelve una lista de los elementos de la variable solo 2 elemetos
    y = int(xy.split()[1])
    icono = bytearray(dibujo.read())  # guardar en matriz de bytes
    dibujo.close()
    return framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)# Datos y tamaño de la imagen.




while True:
    oled.blit(buscar_icono("dibujos/youtube.pbm"), 0, 0) # ruta y sitio de ubicación
    oled.show()
    sleep(1)
    oled.blit(buscar_icono("dibujos/twiter.pbm"), 0, 0) # ruta y sitio de ubicación
    oled.show()
    sleep(1)
  

 
