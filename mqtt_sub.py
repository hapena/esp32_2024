#------------------------------ [IMPORT]------------------------------------

import network, time, urequests
from machine import Pin, ADC, PWM
import utime
import ujson
from umqtt.simple import MQTTClient

#--------------------------- [OBJETOS]---------------------------------------

# MQTT Server Parameters
MQTT_CLIENT_ID = "pepitoEsp23"
MQTT_BROKER    = "broker.hivemq.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
#MQTT_TOPIC_SUB     = b"area/edia/piso1/sen1"
#MQTT_TOPIC_SUB     = b"area/edia/piso2/sen2"
MQTT_TOPIC_SUB     = b"area/edia/#"




#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

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

    

#------------------------------------[MQTT]---------------------------------------------------------------------#

if conectaWifi ("Wokwi-GUEST", ""):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

    def sub_cb(topic, msg):
        print(f"llego el topic: {topic} con el valor {msg}")
        #if topic ==b'area/edia/piso1/sen1':
        #if topic ==b'area/edia/piso2/sen2':
        if topic ==b'area/edia/#':
            dato = msg.decode()
            print(f'Recibido:{dato}')
            print(dato)

    print("Conectando a  MQTT server... ",MQTT_BROKER," ", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.connect()
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(MQTT_TOPIC_SUB)
    print("Conectado!")

    
            

    while True:
        print ("esperando")
        client.wait_msg()
        time.sleep(2)

        
    
        
                
        

else:
       print ("Imposible conectar")
       miRed.active (False)


