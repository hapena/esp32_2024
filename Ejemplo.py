import network, time, urequests
from machine import Pin
from dht import DHT11

sensorDHT = DHT11(Pin(15))
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


if conectaWifi ("Hugo", "Hupe6493"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    url="https://api.thingspeak.com/update?api_key=Q74PAEKYLFZMY3B6"


    while True:
        time.sleep(2)
        sensorDHT.measure()
        temperatura= sensorDHT.temperature()
        humedad= sensorDHT.humidity()
        far= (temperatura*1.8) + 32
        print("Tem={}°c, Hum={}%, Far={}f".format(temperatura,humedad,far))

        respuesta = urequests.get(url+"&field1="+str(temperatura)+"&field2="+str(humedad)+"&field3="+str(far))
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close ()
       



        if temperatura>30:
            led.on()
        else:
            led.off()
    
 
else:
       print ("Imposible conectar")
       miRed.active (False)
