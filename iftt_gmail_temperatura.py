#Envia temperatura y humedad a Drive a traves de ifttA
#https://ifttt.com/maker_webhooks

import network, time, urequests
from dht import DHT11
from machine import Pin

def conectaWifi(red, password):
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


sensorDHT = DHT11 (Pin(15))



if conectaWifi("FAMILIA PENA", "Hupe6493$"):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/mensaje_telegram/with/key/1pLxYy7JQFxTRYOLtH2_O?"  
    url2 = "aca va la url de thinsgpeak"
    
    while (True):
               
        
        time.sleep (4)
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        hum=sensorDHT.humidity()
        print ("T={:02d} ºC, H={:02d} %".format (temp,hum))
        
        
        respuesta_a = urequests.get(url2+"&field1="+str(temp)+"&field2="+str(hum))      
        print(respuesta_a.text)
        print (respuesta_a.status_code)
        respuesta_a.close ()
        
                
        if temp > 23:
                      
            respuesta = urequests.get(url+"&value1="+str(temp)+"&value2="+str(hum))      
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
            
            time.sleep(10)
 
else:
       print ("Imposible conectar")
       miRed.active (False)