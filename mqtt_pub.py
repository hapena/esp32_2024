#------------------------------ [IMPORT]------------------------------------

import network, time, urequests
from machine import Pin, ADC, PWM, reset
import dht
import utime
import ujson
from umqtt.simple import MQTTClient

#--------------------------- [OBJETOS]---------------------------------------

# MQTT Server Parameters
MQTT_CLIENT_ID = "pepitoEsp6"
# MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_BROKER    = "broker.hivemq.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = b"area/edia/piso1/sen1"
MQTT_TOPIC_A   = b"area/edia/piso2/sen2"

sensor = dht.DHT11(Pin(15))


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

if conectaWifi ("FAMILIA PENA", "Hupe6493$"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    
    print("Conectando a  MQTT server... ",MQTT_BROKER,"...", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.connect()

    print("Conectado!")

    nuevo_dato = ""
    nuevo_dato_a = ""

    while True:               
        
        lec_temp = sensor.temperature()
        lec_hum = sensor.humidity()
        
                
        print("Revisando Condiciones ...... ")
        sensor.measure() 
        message = ujson.dumps({
        "Humedad": lec_hum,
        "Temperatura": lec_temp,
        })

        message_A = ujson.dumps({
        "Humedad": lec_hum + 10,
        "Temperatura": lec_temp + 10,
        })

        if message != nuevo_dato:
            
            print("Reportando a  MQTT topic {}: {}".format(MQTT_TOPIC, message))
            client.publish(MQTT_TOPIC, message)
            nuevo_dato = message

        if message_A != nuevo_dato_a:
            print("Reportando a  MQTT topic {}: {}".format(MQTT_TOPIC_A, message_A))
            client.publish(MQTT_TOPIC_A, message_A)
            nuevo_dato_a = message_A
        else:
            print("No hay cambios")
        time.sleep(3)
        
        

else:
       print ("Imposible conectar")
       miRed.active (False)

