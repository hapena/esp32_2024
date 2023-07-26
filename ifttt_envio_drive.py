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
      
    url = "https://maker.ifttt.com/trigger/datos_dht/with/key/bKDBu23LQVH1AXAhsVDQuT?"  
    
    while True:
        #Get security token
        securityUrl = "http://localhost:58000/api/v1/ticket"
        securityData = json.dumps({"username": "cisco","password": "cisco123"})
        securityHeader = {'Content-type': 'application/json'}
        r = urequests.post(securityUrl, data=securityData, headers=securityHeader)
        token = r.json()["response"]["serviceTicket"]
        print("token: " + token)

        #Get hosts
        apiAccessHeader = {}
        apiAccessHeader['content-type'] = 'application/json'
        apiAccessHeader['x-auth-token'] = token
        r = requests.get('http://localhost:58000/api/v1/host', headers=apiAccessHeader);
        print(json.dumps(r.json(), indent=2))
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)