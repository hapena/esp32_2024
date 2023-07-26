#Envia dato a sms android a traves de ifttA
#https://ifttt.com/maker_webhooks

import network, time, urequests
from machine import Pin

def conectaWifi(red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect('FAMILIA PENA', 'Hupe6493$')         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
     return True


push = Pin(13, Pin.IN, Pin.PULL_DOWN)# conectado al positivo  (0)  oprimir (1)
uno = Pin(2, Pin.OUT)

if conectaWifi("FAMILIA PENA", "Hupe6493$"):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/peligro_2/with/key/1pLxYy7JQFxTRYOLtH2_O?"  
    
    while (True):
        
          
        estado = push.value()
        print(estado)
        time.sleep(0.05)
     
    
        if estado == 1:
            uno.value(1)
            respuesta = urequests.get(url+"&value1="+str(uno) +  "Intruso en el Hogar")
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
            
        else:
            uno.value(0)   

        
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)