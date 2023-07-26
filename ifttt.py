import network, time, urequests # wifi, tiempos, enviar datos
from machine import Pin, ADC  # utilizar pines y el potenciometro
import esp32 #utilizar sensores de la tarjeta


sensor = ADC(Pin(36))

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

if conectaWifi ("RedMiHugo", "Hupe6493"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/sensor/with/key/bKDBu23LQVH1AXAhsVDQuT"  
    
    while True:
       
        pot = sensor.read_u16()
        temp = esp32.raw_temperature()   # lee la Tª del microcontrolador en ºFarenheit
        hall = esp32.hall_sensor() # lee el campo magnético perpendicular al  microcontrolador 
        
        
        print("Pote = {}, Tem {}, Campo {}".format (pot, temp, hall))          
        respuesta = urequests.get(url+"&value1="+str(pot)+"&value2="+str(temp)+"&value="+str(hall))
        print(respuesta.text)
        print (respuesta.status_code)
        
else:
       print ("Imposible conectar")
       miRed.active (False)