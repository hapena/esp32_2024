import network, time, urequests
from dht import DHT11
from machine import Pin, ADC

sensor_Hs = ADC(Pin(36))  # Creamis el objeto para realizar la lectura de humedad de suelo
sensor_Hs.width(ADC.WIDTH_12BIT)  # permite regular la precisión de lectura
sensor_Hs.atten(ADC.ATTN_11DB) # permite trabajar con 3.3v
sensorDHT = DHT11 (Pin(15))  # Creamos el objeto DHT11 y asignamos el pin apara leer temperatura
rojo = Pin(2, Pin.OUT)  # Creamos el objeto rojo y asignamos el pin
verde= Pin(4, Pin.OUT)  # Creamos el objeto verde y asignamos el pin



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
      
    url_1 = "https://maker.ifttt.com/trigger/sensor_dth/with/key/1pLxYy7JQFxTRYOLtH2_O?"  
    url_2 = "https://maker.ifttt.com/trigger/correo_emergencia/with/key/1pLxYy7JQFxTRYOLtH2_O?" 
    
    
    
    while (True):
        
        time.sleep (4)
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        hum=sensorDHT.humidity()
        hum_suelo =  int(sensor_Hs.read())
        print ("T={:02d} ºC, H={:02d}, Hs={:02d} = %".format (temp,hum, hum_suelo))
        respuesta_1 = urequests.get(url_1+"&value1="+str(temp)+"&value2="+str(hum)+ "&value3="+str(hum_suelo))      
        print(respuesta_1.text)
        print (respuesta_1.status_code)
        respuesta_1.close ()
        
        if hum_suelo < 300 :
                                    
            respuesta_2 = urequests.get(url_2+"&value1="+str(hum_suelo))      
            print(respuesta_2.text)
            print (respuesta_2.status_code)
            respuesta_2.close ()
            time.sleep(10)
            rojo.value(1)
            verde.value(0)
 
        elif temp> 25 :
                                    
            respuesta_2 = urequests.get(url_2+"&value1="+str(temp))      
            print(respuesta_2.text)
            print (respuesta_2.status_code)
            respuesta_2.close ()
            time.sleep(10)
            rojo.value(1)
            verde.value(0)
            
        else:
            
            rojo.value(0)
            verde.value(1)
            
 
 
 
else:
       print ("Imposible conectar")
       miRed.active (False)