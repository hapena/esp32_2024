import network, time
from machine import Pin
from utelegram import Bot
from dht import DHT11


TOKEN = '5031163680:AAG45iFduorhunFrZs6GsGGBc7QUaegYGhE'
bot = Bot(TOKEN)
sensorDHT = DHT11(Pin(5))
bombillo = Pin(2, Pin.OUT)


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
    
     
    
    @bot.add_message_handler('Inicio')
    def help(update):
        update.reply(''' CASA DOMOTICA \U0001F601
                       \n Menu Casa
                       \n opciones:
                        Temeperatura: 1
                        Encender Iluminación: 2
                        Apagar Iluminación: 3
                        Estado Iluminación: 4
                        
                        \Fin''')
    
    @bot.add_message_handler('1')
    def help(update):
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply('la temperatura de la casa es:'+ str(temp)+" °C")
        
    @bot.add_message_handler('2')
    def help(update):
        bombillo.value(1)
        update.reply("Bombillo Encendido")
    
    @bot.add_message_handler('3')
    def help(update):
        bombillo.value(0)
        update.reply("Bombillo Apagado")
    
    @bot.add_message_handler('4')
    def help(update):
        estado = bombillo.value()
        if estado==1:
            update.reply("Encendido \U0001F60A")
        else:
            update.reply("Apagado \U0001F614 ")
    
    
    bot.start_loop()
 
else:
       print ("Imposible conectar")
       miRed.active (False)