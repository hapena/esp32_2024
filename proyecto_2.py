#Envia temperatura y humedad a Drive a traves de ifttt
#https://ifttt.com/maker_webhooks

import network, time, urequests
from machine import Pin, ADC
from onewire import OneWire
from ds18x20 import DS18X20

ds = DS18X20(OneWire(Pin(4)))
sensor_id = ds.scan()[0]
sensor_a = ADC(Pin(36))
sensor_b = ADC(Pin(39))



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




if conectaWifi("FAMILIA PENA", "Hupe6493$"):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/sensor_dth/with/key/1pLxYy7JQFxTRYOLtH2_O?"  
    
    while (True):
        
        time.sleep(4)
        lectura_a = (sensor_a.read_u16()/65556)*500
        lectura_b = (sensor_b.read_u16()/65536)* 50 -50 -1
        ds.convert_temp()
        tem = ds.read_temp(sensor_id)  
        print("PPM= {:02}, TUR = {:02}, Tem = {:02} ".format(lectura_a,lectura_b,tem))
        respuesta = urequests.get(url+"&value1="+str(lectura_a)+"&value2="+str(lectura_b)+"&value3="+str(tem))      
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
 
else:
       print ("Imposible conectar")
       miRed.active (False)