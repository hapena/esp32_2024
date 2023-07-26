from machine import Pin
from utime import sleep
from dht import DHT11

sensorDHT= DHT11(Pin(15))


while True:
    
    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    
    
    print("T={:02d}C H={:02d}%".format(temp, hum))
    
    