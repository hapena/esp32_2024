import umail



smtp = umail.SMTP('smtp.gmail.com', 587, username='my@gmail.com', password='mypassword')
smtp.to('someones@gmail.com')
smtp.send("This is an example.")
smtp.quit()

import umail
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
smtp.login('bob@gmail.com', 'bobspassword')
smtp.to('alice@gmail.com')
smtp.write("From: Bob <bob@gmail.com>\n")
smtp.write("To: Alice <alice@gmail.com>\n")
smtp.write("Subject: Poem\n\n")
smtp.write("Roses are red.\n")
smtp.write("Violets are blue.\n")
smtp.write("...\n")
smtp.send()
smtp.quit()
***********************************************************
from umail import SMTP
import network, time

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

if conectaWifi ("red", "contraseña"):
      print ("Conexión exitosa!")
      print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
      smtp = SMTP('smtp.gmail.com', 587, username='usuario@gmail.com', password='contraseña')
      smtp.to('profetolocka@gmail.com')
      smtp.send("Hola mundo!")  
      smtp.quit()  
      miRed.active (False)

 else:
      print ("Imposible conectar")