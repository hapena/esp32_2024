#Aqui se define Modulos
from machine import Pin, I2C
import _thread
import network, time, urequests, sh1106
from HCSR04 import HCSR04
import bluetooth
from BLE import BLEUART

ancho = 128
alto = 64
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = sh1106.SH1106_I2C(ancho, alto, i2c)


#print(i2c.scan())
#Definicion de pines led semaforo1
led_red = Pin(16, Pin.OUT)
led_orange = Pin(17, Pin.OUT)
led_green = Pin(5, Pin.OUT)
#Definicion de pines led semaforo2
led_red1 = Pin(12, Pin.OUT)
led_orange1 = Pin(14, Pin.OUT)
led_green1 = Pin(23, Pin.OUT)

#Sensores medidores de distancia
#Sensor que apunta hacia los vehiculos
sensor1 = HCSR04(trigger_pin=15, echo_pin=2, echo_timeout_us=10000)
#sensor detras semaforo
sensor2 = HCSR04(trigger_pin=33, echo_pin=32, echo_timeout_us=10000)
#sensor final de la calle
sensor3 = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=10000)

#Aqui se define los sensores infrarrojos
sensor8 = Pin(25, Pin.IN, Pin.PULL_DOWN)
sensor9 = Pin(9, Pin.IN, Pin.PULL_DOWN)
sensor10 = Pin(13, Pin.IN, Pin.PULL_DOWN)


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

def leds(a,b,c,d,e,f):
    led_red.value(a)
    led_orange.value(b)
    led_green.value(c)
    led_red1.value(d)
    led_orange2.value(e)
    led_green3.value(f)



if conectaWifi ("ReydeCopas666", "Nacional666"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
          
    url = "https://api.thingspeak.com/update?api_key=0VH9TN4OG35FQOAG"
    url2 = "https://api.thingspeak.com/update?api_key=0VH9TN4OG35FQOAG"  # la de drive
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def nucleo_dos_semaforo():
        
        estado_sem = sensor8.value()
        estado_sem1 = sensor9.value()
        estado_sem2 = sensor10.value()
        print(estado_sem, estado_sem1, estado_sem2)
        time.sleep(0.01)
        
            
        while True:
            
             if estado_sem == 0 and estado_sem1 == 0 and  estado_sem2 == 0:
                 
                 leds(1,0,0,0,0,1)
                 utime.sleep(3)
                 leds(0,1,0,0,1,0)
                 utime.sleep(3)
                 leds(0,0,1,1,0,0)
                 utime.sleep(3)
                 leds(0,1,0,0,1,0)
                 utime.sleep(3)
                 
            else:    
                 leds(1,0,0,0,0,1)
                 utime.sleep(0.1)
                 leds(0,1,0,0,1,0)
                 utime.sleep(0.1)
                 leds(0,0,1,1,0,0)
                 utime.sleep(0.1)
                 leds(0,1,0,0,1,0)
                 utime.sleep(0.1)
            
        

    _thread.start_new_thread(nucleo_dos_semaforo,())


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    def nucleo_tres_oled():
        
        distance1 = int(sensor1.distance_cm())
        print("Sensor que apunta hacia los vehiculos :" ,distance1 , "cm")         
        distance2 = int(sensor2.distance_cm())
        print("sensor detras semaforo" ,distance2, "cm")                   
        distance3 = int(sensor3.distance_cm())
        print("sensor final: " ,distance3, "cm")
        
               
        if distance1 <= 80:
            print("Hay presencia de Vehiculos")
            
        elif distance2 <= 8:
            print("Hay trancon")
            respuesta2 = urequests.get(url2+"&field1="+str("TRANCON EN VIA"))
            print(respuesta2.text)
            print (respuesta2.status_code)
            respuesta2.close()
            
        elif distance3 <= 15:
            print("Todavia sigue el trancon")
        
        else:
            print("Via Libre")
            

        oled.fill(0)
        oled.text("D1: ", 0, 0)
        oled.text(str(distance1), 60, 0)
        oled.text("D2: ", 0, 10)
        oled.text(str(distance2), 60, 10)
        oled.text("D3: ", 0, 20)
        oled.text(str(distance3), 60, 20)
        oled.show()
        
        respuesta = urequests.get(url+"&field1="+str(distance1)+"&field2="+str(distance2)+"&field3="+str(distance3))
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close()
        
        _thread.start_new_thread(nucleo_tres_oled,())
        
        
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    while True:
        
        
        estado1 = sensor8.value()#cerca al semaforo - primer sensor
        estado2 = sensor9.value()#segundo sensor - del medio
        estado3 = sensor10.value()#sensor final -tercer
        
        if (estado1 == 1 and estado2 == 1 and estado3 == 1) or (estado1 == 1 and estado2 == 1 and estado3 == 0):
            print("Via Libre", estado1, estado2, estado3)
        
        
    
else:
    print ("Imposible conectar")
    miRed.active (False)    
             