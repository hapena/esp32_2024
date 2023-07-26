#------------------------------ [IMPORT]------------------------------------
import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from dht import DHT11
import utime
import _thread

TOKEN = '5565503624:AAGWq4TuVKOPLqaa5nJVp4l_Rv5cYWUkRaY' # Token de su bot telegram

#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)

sensorDHT= DHT11(Pin(4))

gas =   ADC(Pin(39))
gas.width(ADC.WIDTH_10BIT) 
gas.atten(ADC.ATTN_11DB)

luz = ADC(Pin(36))
luz.width(ADC.WIDTH_10BIT) 
luz.atten(ADC.ATTN_11DB)

lluvia = ADC(Pin(34))
lluvia.width(ADC.WIDTH_10BIT) 
lluvia.atten(ADC.ATTN_11DB)

caudal = ADC(Pin(35))
caudal.width(ADC.WIDTH_10BIT) 
caudal.atten(ADC.ATTN_11DB)

ventilador = Pin(19, Pin.OUT)

bombillo  = Pin(5, Pin.OUT)

puerta = PWM(Pin(12), freq=50)

magnetico = Pin(15,Pin.IN,Pin.PULL_UP) # conectado al negativo (1)  oprimir (0)


#----------------------[ SERVO-MOTOR ]---------------------------------------------------------#

def map(x):
        return int((x - 0) * (125- 25) / (180 - 0) + 25)
    
    
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

 
#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("Hugo", "Hupe6493"):  # Datos de su red SSID y password 

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
        
    
    url = "https://api.thingspeak.com/update?api_key=T22D86IN1PMTEF2Z" # uri de su canal https://thingspeak.com
    
    while True:
        lectura_gas = gas.read()
        lectura_luz = luz.read()
        lectura_lluvia = lluvia.read()
        caudalimetro = caudal.read()
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity() 
        print("Gas=", lectura_gas, "luz=", lectura_luz, "lluv=", lectura_lluvia,"Cau=", caudalimetro, "tem=", temp, "hum", hum)
        respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum))#+"&field3="+str(lectura_gas)+"&field4="+str(lectura_luz)+"&field5="+str(lectura_lluvia)+"&field6="+str(caudalimetro))
        print(respuesta.status_code)
        respuesta.close() 
        utime.sleep(4)
           
    
else:
       print ("Imposible conectar")
       miRed.active (False)
