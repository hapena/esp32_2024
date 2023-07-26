from dht import DHT11
from machine import Pin
from utime import sleep

sensorDHT = DHT11(Pin(15))

while True:

    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    kelvin = temp + 273
    far = (temp*9)/5 + 32

    print("T={:02d}C H={:02d}%  K= {:02d}k F={:02}".format(temp, hum, kelvin,far))


