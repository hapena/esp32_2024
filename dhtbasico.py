from machine import Pin
from utime import sleep
from dht import DHT11

sensorDHT = DHT11(Pin(4))

#file = open("sensores.csv", "w")

while True:
    
    sleep(1)
    sensorDHT.measure()
    tem = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    kel = tem + 273.15
    far = (tem *9)/5 + 32
    #file.write(str("T={:02.1f}°c ; H={:02.1f}% ; K={:02.2f}k ; F={:02.2f}f \n ".format(tem, hum, kel, far)))
    #file.flush()
    print("T={:02.1f}°c , H={:02.1f}% , K={:02.2f}k , F={:02.2f}f  ".format(tem, hum, kel, far))
    
    
    
    