from machine import Pin
import bluetooth
from BLE import BLEUART

bombillo= Pin(15, Pin.OUT)

name= "EspHugo" 

ble = bluetooth.BLE()
uart = BLEUART(ble, name)

print (name, "aca ok")

def on_rx():
    
    rx_recibe = uart.read().decode().strip() # leer, decodificar utf8,elimina espacios
    uart.write("EspHugo dice: " + str(rx_recibe) + "\n")
    
    if rx_recibe == "on":
        bombillo.value(1)
        print("encendiendo bombillo")
        uart.write("EspHugo dice: " + "encendiendo" + "\n")
        
    if rx_recibe == "off":
        bombillo.value(0)
        print("apagando bombillo")
        uart.write("EspHugo dice: " + "apagando" + "\n")
    
    
uart.irq(handler = on_rx) # controlador de interrupciones, a quien llamar cuando el pin se active