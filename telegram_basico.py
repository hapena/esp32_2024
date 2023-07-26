#------------------------------ [IMPORT]------------------------------------


import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from dht import DHT11
import utime

TOKEN = '5565503624:AAGWq4TuVKOPLqaa5nJVp4l_Rv5cYWUkRaY'

#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)
bombillo  = Pin(15, Pin.OUT)
sensorDHT = DHT11(Pin(4))
servo = PWM(Pin(5), freq=50)


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

def map(x):
    return int((x - 0) * (125 - 25) / (180 - 0) + 25)
    

#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("FAMILIA PENA", "Hupe6493$"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    print("ok")
    
    @bot.add_message_handler("Inicio")
    def help(update):
        update.reply('''¡Estación Metereológica! \U0001F600
                     \n Menu Principal
                     \n Elije una opción:
                     
                     Temperatura  \U0001F605: 1
                     Humedad: 2
                     Encender Iluminación : On
                     Apagar Iluminación \U0001F643: Off
                     Abrir Puerta : Open
                     Cerrar Puerta : Close
                     Estado Iluminación \U0001F642: Estado
                     
                     \n No olvides que estoy para ayudarte''')
    
    @bot.add_message_handler("1")
    def help(update):
        sensorDHT.measure()
        tem = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply("La temperatura es," + str(tem) + "°c")
                     
        
    @bot.add_message_handler("2")
    def help(update):
        sensorDHT.measure()
        tem = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply("La Humedad es," + str(hum) + "%")
        
    @bot.add_message_handler("On")
    def help(update):
        bombillo.value(1)
        update.reply("Encendiendo")
        
    @bot.add_message_handler("Off")
    def help(update):
        bombillo.value(0)
        update.reply("Apagando")
    
    @bot.add_message_handler("Open")
    def help(update):
        m = map(180)
        servo.duty(m)
        update.reply("Puerta Abierta")
    
    @bot.add_message_handler("Close")
    def help(update):
        m = map(0)
        servo.duty(m)
        update.reply("Puerta Cerrada")
        
    @bot.add_message_handler("Estado")
    def help(update):
        estado = bombillo.value()
        if estado == 1:
            update.reply("Bombillo encendido")
        else:
            update.reply("Bombillo Apagado")
        
    
    
    
    
    bot.start_loop()
    
      

else:
       print ("Imposible conectar")
       miRed.active (False)