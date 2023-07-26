from machine import Pin
import bluetooth
from BLE import BLEUART
import utime
from dht import DHT11

sensorDHT = DHT11(Pin(5))


name="EspHugo"
print (name, "aca OK")

ble = bluetooth.BLE()
uart = BLEUART(ble,name)

def on_rx():
    rx_recibe = uart.read().decode().strip()
    uart.write("Esp32 dice:" + str(rx_recibe)  + "\n")  
    print(rx_recibe)                                    



while True:
    sensorDHT.measure()
    tem = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    uart.write(str(tem)+","+str(hum)+ " \n" )
    utime.sleep(0.1)
    uart.irq(handler= on_rx)
    