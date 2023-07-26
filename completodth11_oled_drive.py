from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
from utime import sleep
import network, time, urequests


sensorDHT = DHT11(Pin(15))
file = open("otro.csv", "w")

ancho = 128
alto = 64
nombre = "hugo_pena"

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())
 
oled.text('Welcome to the', 0, 0)
oled.text('Areandina', 0, 10)
oled.text('Control de Temperatura', 0, 20)
oled.show()
sleep(2)
 

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


sensorDHT = DHT11 (Pin(15))

if conectaWifi("FAMILIA PENA", "Hupe6493$"):
    

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/sensor_dth/with/key/1pLxYy7JQFxTRYOLtH2_O?"  


    while True:
    
        sleep(2)
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        kelvin = temp + 273
        file.write(str("T={:02d} ºC, H={:02d} %  K= {:02d} k   ".format(temp, hum, kelvin) ))
        file.flush()
        oled.fill(0)
        oled.text("Temperatura:",0,10)
        oled.text(str(temp),100,10)
        oled.text("Humedad:",0,20)                
        oled.text(str(hum),100,20)
        oled.text("Kelvin:",0,30)                
        oled.text(str(kelvin),100,30) 
        oled.show()
    
        print("T={:02d} ºC, H={:02d} %  K= {:02d} k".format(temp, hum, kelvin))
        sleep(0.25)
        
        respuesta = urequests.get(url+"&value1="+str(temp)+"&value2="+str(hum) + "&value3="+ str(nombre) )      
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
        
        
        
        
else:
       print ("Imposible conectar")
       miRed.active (False)
        
        