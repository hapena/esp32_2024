from machine import Pin
import bluetooth
from BLE import BLEUART

led_b = Pin(12, Pin.OUT)



name="Esp32Hugo"

ble = bluetooth.BLE()
uart = BLEUART(ble,name)

def on_rx():
    rx_recibe = uart.read().decode().strip()# leer , decodifica y elimina espacios 
    uart.write("Esp32 dice:" + str(rx_recibe)  + "\n")
    
    if rx_recibe == "a":
        led_b.value(1)
        
    if rx_recibe == "b":
        led_b.value(0)
        
    
uart.irq(handler= on_rx)
    
    
    