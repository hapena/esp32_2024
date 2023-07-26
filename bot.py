#------------------------------ [IMPORT]------------------------------------


import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
import utime

TOKEN = '5031163680:AAG45iFduorhunFrZs6GsGGBc7QUaegYGhE'

#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)
bombillo  = Pin(5, Pin.OUT)


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

if conectaWifi ("Hugo", "Hupe6493"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    
    @bot.add_message_handler("Hola")
    def help(update):
        update.reply('''¡Bienvenido!
                     \n Menu Principal
                     \n Ejmemplo
                     \n Elije una opción:
                     
                     Nombre  : 1
                     Edad: 2
                     Estado Civil: 3
                     
                     \n No olvides que estoy para ayudarte''')
    
    @bot.add_message_handler("1")
    def help(update):
        update.reply('''¡Bienvenido!
                     \n Nombre:
                     \n Hugo Peña
                     
                     \n No olvides que estoy para ayudarte''')
        
    @bot.add_message_handler("2")
    def help(update):
        update.reply('''¡Bienvenido!
                     \n Edad
                     \n 22 Años
                     
                     \n No olvides que estoy para ayudarte''')
    
    
    
    bot.start_loop()
    
      

else:
       print ("Imposible conectar")
       miRed.active (False)