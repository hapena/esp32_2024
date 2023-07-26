#------------------------------ [IMPORT]------------------------------------
import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from dht import DHT11
import utime

TOKEN = '5031163680:AAG45iFduorhunFrZs6GsGGBc7QUaegYGhE'

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
        return int((x - 0) * (130- 34) / (180 - 0) + 34)
    
    
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
    
    url = "https://api.thingspeak.com/update?api_key=T22D86IN1PMTEF2Z" 
    
    while True:
        
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        lectura_gas = gas.read()
        lectura_luz = luz.read()
        lectura_lluvia = lluvia.read()
        caudalimetro = caudal.read() 
        
        
        r = urequests.get(url+"&field1="+str(temp)+
                          "&field2="+str(hum)+
                          "&field3="+str(lectura_gas)+
                          "&field4="+str(lectura_luz)+
                          "&field5="+str(lectura_lluvia)+
                          "&field6="+str(caudalimetro))
        print(r.status_code)
        r.close ()
        
                  
        @bot.add_message_handler("Hola")
        def help(update):
            update.reply('''¡Bienvenido! 
                         \n Menu Principal                                        
                         \n Domotic Control House U0001F916
                         \n Estado de tu Hogar...... 
                         \n Elije una opción:
                         
                         Temperatura : Temp U0001F912
                         Gas: Gas U0001F480
                         Luz Dia: Luz U0001F60E
                         Lluvia y Humedad: Clima U0001F976
                         Consumo de Agua: Caudal U0001F62D
                         Activar Aire A: Airea U0001F44D
                         Deasactivar Aire A:Aired U0001F44E
                         Encender Iluminacion : On  U0001F44D
                         apagar Iluminacion : Off  U0001F44E
                         Abrir Puerta: Open  U0001F44D
                         Cerrar Puerta : Close U0001F44E
                         Estado Puerta: Estado U0001F91A
                         Ver DashBoard: Ver U0001F4BB
                                                                                                
                         \n No olvides que estoy para tu seguridad y confort
                         \n garcias  U0001F600''')
              
        
        @bot.add_message_handler("Temp")
        def sensor_temperatura(update):
                              
            update.reply("Temperatura: "+ str(temp) + "°C  " + "Humedad: " + str(hum) + "%")
            
        
        @bot.add_message_handler("Gas")
        def sensor_gas(update):
                        
            if lectura_gas > 600:
                update.reply("Gas: "+ str(lectura_gas) + " Nivel Alto")
            else:
                update.reply("Gas: "+ str(lectura_gas) + " Nivel Normal")
                
        @bot.add_message_handler("Luz")
        def sensor_luz(update):
            
            if lectura_luz < 600:
                update.reply("Nivel Luminosidad: "+ str(lectura_luz) + " Dia")
            else:
                update.reply("Nivel Luminosidad: "+ str(lectura_luz) + " Noche")
                
        @bot.add_message_handler("Clima")
        def sensor_lluvia(update):
                        
            if lectura_lluvia > 100:
                update.reply("Clima: "+ str(lectura_lluvia) + " Clima lluviosos")
            else:
                update.reply("Clima "+ str(lectura_lluvia) + " clima Seco")
                
        @bot.add_message_handler("Caudal")
        def sensor_caudal(update):
                       
            update.reply("El caudal es"+ str(caudalimetro))     
             
        @bot.add_message_handler("Airea")
        def activar_aire(update):
            ventilador.off()
            update.reply("Aire Acondicionado Encendido")
            
        @bot.add_message_handler("Aired")
        def desactivar_aire(update):
            ventilador.on()
            update.reply("Aire Acondicionado apagado")
            
        @bot.add_message_handler("On")
        def activar_iluminacion(update):
            bombillo.off()
            update.reply("Iluminación Encendido")
            
        @bot.add_message_handler("Off")
        def desactivar_ilumunacion(update):
            bombillo.on()
            update.reply("Iluminación apagado")
            
        @bot.add_message_handler("Open")
        def abrir_puerta(update):
            m = map(180)
            puerta.duty(m)
            update.reply("Puerta Abierta")
            
        @bot.add_message_handler("Close")
        def cerrar_puerta(update):
            m = map(90)
            puerta.duty(m)
            update.reply("Puerta Cerrada")
            
        @bot.add_message_handler("Estado")
        def estado_puerta(update):
                        
            estado = magnetico.value()
            utime.sleep(0.2)
            
            if estado == 1:
                update.reply("Estado de la puerta: 'Cerrada' ")
            else:
                update.reply("Estado de la puerta: 'Abierta' ")
                
        @bot.add_message_handler("Ver")
        def dashboard(update):
                       
            update.reply("https://thingspeak.com/channels/1807893") 
         
                      
        bot.start_loop()
    
else:
       print ("Imposible conectar")
       miRed.active (False)