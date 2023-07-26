#Envia temperatura y humedad a Gamil a traves de ifttA
#https://ifttt.com/maker_webhooks

import network, time, urequests
import esp32
from machine import Pin


led = Pin(2, Pin.OUT)

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
      
    url = "https://maker.ifttt.com/trigger/correo_emergencia/with/key/1pLxYy7JQFxTRYOLtH2_O?"  
    
    while (True):
        
        time.sleep (4)
        temp = esp32.raw_temperature()   # lee la Tª del microcontrolador en ºFarenheit
        hall = esp32.hall_sensor() # lee el campo magnético perpendicular al  microcontrolador (1.5uds = 1mT) mT = miliTesla                
        print ("Tem={:02d} ºF, Mag={:02d} Tesla".format(temp,hall))
        
        if temp > 120:
            respuesta = urequests.get(url+"&value1="+str(temp)+"&value2="+str(hall))      
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
            led.value(1)
            
        else:
            led.value(0)
            
            
else:
       print ("Imposible conectar")
       miRed.active (False)