import network, time, urequests
from machine import Pin, ADC
from utelegram import Bot
from dht import DHT11


TOKEN = '5031163680:AAG45iFduorhunFrZs6GsGGBc7QUaegYGhE'

bot = Bot(TOKEN)
led = Pin(6, Pin.OUT)
sensorDHT= DHT11(Pin(15))

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
      
    @bot.add_message_handler('Hola')
    def help(update):
        update.reply('Escriba on para encender y off para apagar el led, Value para estado y Sensor para temperatura')

    @bot.add_message_handler('Value')
    def value(update):
        if led.value():
            update.reply('LED is on')
        else:
            update.reply('LED is off')

    @bot.add_message_handler('On')
    def on(update):
        led.on()
        update.reply('LED is on')

    @bot.add_message_handler('Off')
    def off(update):
        led.off()
        update.reply('LED is off')
        
    @bot.add_message_handler('Sensor')
    def lectura_sensor(update):
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()       
        print("T={:02d}C H={:02d}%".format(temp, hum))
        update.reply('Temp: '+ str(temp) + 'Hum: ' + str(hum))
        
        
    
    
    bot.start_loop()
        
        
    
        
        
        
        
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)