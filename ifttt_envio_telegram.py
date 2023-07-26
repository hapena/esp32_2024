import network, time, urequests
import json
from dht import DHT11
from machine import Pin

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

sensorDHT = DHT11(Pin(5))

if conectaWifi ("FAMILIA PENA", "Hupe6493$"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/telegram/with/key/bKDBu23LQVH1AXAhsVDQuT?"  
    
    while True:
        time.sleep(4)
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        hum=sensorDHT.humidity()
        print ("T={} ºC, H={} %".format(temp,hum))
        
        if temp>27:
        
            respuesta = urequests.get(url+"&value1="+str(temp)+"&value2="+str(hum))
            print(respuesta.text)
            print(respuesta.status_code)
            respuesta.close ()
            
        time.sleep(1)
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)