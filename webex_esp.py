import network, time, urequests
from machine import Pin
import ujson

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


Key = 'Bearer YmM4NGI3MjUtODZhOC00Y2YzLWFhZjEtMGVkNTA3OThmMGU5OTE1OGU2ZDktMjBh_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457'




if conectaWifi ("FAMILIA PENA", "Hupe6493$"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    #url = "https://api.thingspeak.com/update?api_key=P36P1BXYGPLAPACT"  
    
    while True:
        time.sleep(4)
        

        respuesta = urequests.get("https://webexapis.com/v1/rooms",
                    headers={'Authorization':Key})
        
        rooms = respuesta.json()['items']    
        roomIdToMessage = None
        roomNameToSearch = 'ejemploiot'
        
        for room in rooms:
            if(room['title'].find(roomNameToSearch) != -1):
                print ("Encontrando Salas  " + roomNameToSearch)
                print ("Nombre de sala: '" + room['title'] + "' ID: " + room['id'])
                roomIdToMessage = room['id']
                roomTitleToMessage = room['title']
            break
        
        lastMessageId = None
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close ()
 
else:
       print ("Imposible conectar")
       miRed.active (False)