import network, time, urequests
from machine import Pin
import json

led = Pin(2, Pin.OUT)

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


if conectaWifi ("FAMILIA PENA", "Hupe6493$"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://api.thingspeak.com/channels/1794528/feeds.json?results=2"  
    
    while True:
        
        
        consulta=urequests.get(url)
        datos=consulta.json()
        print (datos)
        tem=datos["feeds"][1]["field1"]
        hum=datos["feeds"][1]["field2"]
        dis=datos["feeds"][1]["field3"]
        print("Tem={}°C, Hum={}%, Dis={}cm".format(tem,hum, dis))
        tempe = float(tem)
        time.sleep(1)
        
        if tempe > 30:
            led.value(1)
        else:
            led.value(0)
 
else:
       print ("Imposible conectar")
       miRed.active (False)