import network, time
import json
from machine import Pin
import socket


led = Pin(2,Pin.OUT)

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
      
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',80)) # specifies that the socket is reachable 
    s.listen(5)     # max of 5 socket connections
    
    def web_page():
        if led.value()==1:
            led_state = 'ON'
            print('led is ON')
        elif led.value()==0:
            led_state = 'OFF'
            print('led is OFF')

        html_page = """   
          <html>   
          <head>   
           <meta content="width=device-width, initial-scale=1" name="viewport"></meta>   
          </head>   
          <body>   
            <center><h2>ESP32 Web Server Hugo Sparkfun ESP32-S2 </h2></center>   
            <center>   
             <form>   
              <button name="LED" type="submit" value="1"> LED ON </button>   
              <button name="LED" type="submit" value="0"> LED OFF </button>   
             </form>   
            </center>   
            <center><p>LED is now <strong>""" + led_state + """</strong>.</p></center>   
          </body>   
          </html>"""  
        return html_page   
    
    
    
    
    while True:
        # Socket accept() 
        conn, addr = s.accept()
        print("Got connection from %s" % str(addr))
        
        # Socket receive()
        request=conn.recv(1024)
        print("")
        print("")
        print("Content %s" % str(request))

        # Socket send()
        request = str(request)
        led_on = request.find('/?LED=1')
        led_off = request.find('/?LED=0')
        if led_on == 6:
            print('LED ON')
            print(str(led_on))
            led.value(1)
        elif led_off == 6:
            print('LED OFF')
            print(str(led_off))
            led.value(0)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        
        # Socket close()
        conn.close()
            
 
else:
       print ("Imposible conectar")
       miRed.active (False)