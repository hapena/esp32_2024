import network, time, urequests
from machine import Pin
from utime import sleep, sleep_ms
import ujson
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "alex333333333"
MQTT_BROKER    = "broker.hivemq.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC_SUB     = "andina/python/noche"


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


if conectaWifi("Wokwi-GUEST", ""):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    print("Conectando a  MQTT server... ",MQTT_BROKER,"...", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.connect()

    print("Conectado!")

    def sub_cb(topic, msg):
        print(f"llego el topic: {topic} con el valor {msg}")
        if topic == b'andina/python/noche':
            dato = msg.decode()
            print(f'Recibido:{dato}')
            print(dato)


    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(MQTT_TOPIC_SUB)
    

    while True:
        print ("esperando")
        client.wait_msg()
        time.sleep(2)
       
else:
       print ("Imposible conectar")
       miRed.active (False)

