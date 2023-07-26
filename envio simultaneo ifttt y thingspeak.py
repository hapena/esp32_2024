import network, time, urequests
from dht import DHT11
from machine import Pin, PWM, ADC

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


sensorDHT = DHT11 (Pin(15))

buzzer=PWM(Pin(5))



if conectaWifi("SSID", "Password"):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url_1= "https://maker.ifttt.com/trigger/mensaje_telegram/with/key/1pLxYy7JQFxTRYOLtH2_O?" # url de ifttt 
    url_2 = "https://api.thingspeak.com/update?api_key=SOZVP9W39N8PEKDR" # url de thingspeak
    
    while True:
               
        
        time.sleep (4)
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        hum=sensorDHT.humidity()
        print ("T={:02d} ºC, H={:02d} %".format (temp,hum))
        
        
        envio_thingspeak = urequests.get(url_2+"&field1="+str(temp)+"&field2="+str(hum))      
        print(envio_thingspeak.text, envio_thingspeak.status_code)
        envio_thingspeak.close ()
        
                
        if temp > 23:
                      
            envio_ifttt = urequests.get(url_1+"&value1="+str(temp)+"&value2="+str(hum))      
            print( envio_ifttt.text, envio_ifttt.status_code)
            envio_ifttt.close ()
            buzzer.freq(261)
            buzzer.duty(1023)
            
 
else:
       print ("Imposible conectar")
       miRed.active (False)