import network, time, urequests
from machine import Pin
import ntptime
from time import localtime


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


if conectaWifi ("FAMILIA PENA", "Hupe6493$"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    print ("valores con hora del computador")
    print (localtime())
    hora_local=f"{localtime()[3]:02d}:{localtime()[4]:02d}:{localtime()[5]:02d}"
    fecha_local=f"{localtime()[0]:02d}/{localtime()[1]:02d}/{localtime()[2]:02d}"
    print (f"la hora es: {hora_local}")
    print (f"la fecha es: {fecha_local}")
    print ("*"*45)

    
    print ("valores con NTP")
    ntptime.settime()
    print (localtime())
    hora_ntp=f"{localtime()[3]:02d}:{localtime()[4]:02d}:{localtime()[5]:02d}"
    fecha_ntp=f"{localtime()[0]:02d}/{localtime()[1]:02d}/{localtime()[2]:02d}"
    print (f"la hora es: {hora_ntp}")
    print (f"la fecha es: {fecha_ntp}")
    print ("*"*45)
 
 
else:
       print ("Imposible conectar")
       miRed.active (False)