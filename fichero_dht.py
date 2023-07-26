from machine import Pin
from utime import sleep
from dht import DHT11

sensorDHT= DHT11(Pin(15))

file = open("dato.csv", "w")


while True:
    
    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    
    file.write(str("T={:02}C H={:02}% \n".format(temp, hum)))
    file.flush()
               
    print("T={:02d}C H={:02d}%".format(temp, hum))