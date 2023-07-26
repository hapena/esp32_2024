from dht import DHT11
from machine import Pin
from utime import sleep

sensorDHT = DHT11(Pin(15))

file = open("lecturas.csv", "w")

while True:
    sleep(2)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity() 
    kelvin = temp + 273
    file.write(str("T={:02d}ºC ; H={:02d}% ; K={:02d}k \n".format(temp, hum, kelvin)))
    file.flush()

    print("T={:02d}ºC, H={:02d}%  K= {:02d}k".format(temp, hum, kelvin))

    