from dht import DHT11
from machine import Pin
from utime import sleep

sensorDHT = DHT11(Pin(15))

while True:

  
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    far = (temp*5)/9 + 32
   

    print("T={:02.2f}C H={:02.2f}%  F= {:02.2f}F".format(temp, hum,  far))


