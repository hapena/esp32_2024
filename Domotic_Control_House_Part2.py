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
    
    '''def api_envio():
    
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
           
    _thread.start_new_thread(api_envio, ())'''
   
    
    
    @bot.add_message_handler("Inicio")
    def help(update):
        update.reply('''¡Bienvenido! 
                \n Menu Principal                                        
                \n Domotic Control House \U0001F916
                \n Elije una opción:
                        
            Temperatura : Temperatura 
            Humedad : Humedad 
            Gas: Gas 
            Luz Dia: Luz
            Lluvia y Humedad: Clima 
            Consumo de Agua: Caudal 
            Activar Aire A: Airea 
            Deasactivar Aire A:Aired 
            Encender Iluminacion : On 
            apagar Iluminacion : Off  
            Abrir Puerta: Open 
            Cerrar Puerta : Close 
            Estado Puerta: Estado 
                                                                                                                        
                \n No olvides que estoy para tu seguridad y confort
                \n Gracias  \U0001F600
                \n Ver en línea tu DashBoard: 
                \n https://thingspeak.com/channels/1807893''')
            
    
    @bot.add_message_handler("Temperatura")
    def sensor_temperatura(update):
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()              
        update.reply("Temperatura: "+ str(temp) )
        print("ok Tem")
        utime.sleep(2)
    

    @bot.add_message_handler("Humedad")
    def sensor_huemedad(update):
        sensorDHT.measure()
        hum = sensorDHT.humidity()              
        update.reply("Humedad: " + str(hum))
        print("ok Humedad")
        utime.sleep(2)

    
    @bot.add_message_handler("Gas")
    def sensor_gas(update):
        lectura_gas = gas.read()          
        if lectura_gas > 600:
            update.reply("Gas: "+ str(lectura_gas) + " Nivel Alto")
        else:
            update.reply("Gas: "+ str(lectura_gas) + " Nivel Normal")
        print("ok Gas")    

    @bot.add_message_handler("Luz")
    def sensor_luz(update):
        lectura_luz = luz.read()
        if lectura_luz < 600:
            update.reply("Nivel Luminosidad: "+ str(lectura_luz) + " Dia")
        else:
            update.reply("Nivel Luminosidad: "+ str(lectura_luz) + " Noche")

        print("ok Luz")

    @bot.add_message_handler("Clima")
    def sensor_lluvia(update):
        lectura_lluvia = lluvia.read()            
        if lectura_lluvia > 100:
            update.reply("Clima: "+ str(lectura_lluvia) + " Clima lluviosos")
        else:
            update.reply("Clima "+ str(lectura_lluvia) + " clima Seco")

        print("ok Clima")

    @bot.add_message_handler("Caudal")
    def sensor_caudal(update):
        caudalimetro = caudal.read()            
        update.reply("El caudal es"+ str(caudalimetro))     
        print("ok Caudal")

    @bot.add_message_handler("Aired")
    def activar_aire(update):
        ventilador.on()
        update.reply("Aire Acondicionado apagado")
        print("ok Aired")

    @bot.add_message_handler("Airea")
    def desactivar_aire(update):
        ventilador.off()
        update.reply("Aire Acondicionado encendido")
        print("ok Airea")

    @bot.add_message_handler("Off")
    def activar_iluminacion(update):
        bombillo.on()
        update.reply("Iluminación Apagada")
        print("ok Iluminacion off")

    @bot.add_message_handler("On")
    def desactivar_ilumunacion(update):
        bombillo.off()
        update.reply("Iluminación encendida")
        print("ok Iluminacion on")
        
    @bot.add_message_handler("Open")
    def abrir_puerta(update):
        m = map(180)
        puerta.duty(m)
        update.reply("Puerta Abierta")
        print("ok puerta on")
        
    @bot.add_message_handler("Close")
    def cerrar_puerta(update):
        m = map(90)
        puerta.duty(m)
        update.reply("Puerta Cerrada")
        print("ok puerta off")
        
    @bot.add_message_handler("Estado")
    def estado_puerta(update):
                    
        estado = magnetico.value()
        utime.sleep(0.2)
        
        if estado == 1:
            update.reply("Estado de la puerta: 'Cerrada' ")
        else:
            update.reply("Estado de la puerta: 'Abierta' ")

        print("ok magnetico")  
    
                    
    bot.start_loop()
    


else:
       print ("Imposible conectar")
       miRed.active (False)