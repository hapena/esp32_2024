#Programa desarrollado por Wilson Perezpara manejar el Joystick KY-023

# Módulos a trabajar:

from machine import Pin, ADC, PWM
import utime

# definición de pines para ESP32 de 38 pines para señales de entrada

sw= ADC (Pin(34))  # SW Pulsador
vrx= ADC (Pin(32)) # vrx Colocar color Verde
vry= ADC (Pin(33)) # Azul Colocar color Azul

# definición de pines para ESP32 de 38 pines de salidas actuadores

led=Pin(2, Pin.OUT) # Colocar color morado
ledIzRojo=Pin(16, Pin.OUT) # Colocar color Rojo
ledDrVerde=Pin(17, Pin.OUT) # Colocar color Verde derecha eje x
ledAbAmarillo=Pin(18, Pin.OUT) # Colocar color Amarillo eje y abajo
ledArAzul=Pin(19, Pin.OUT) # Colocar color Azul arriba eje y
    

# Atenuación de la tarjeta a 3.3v

vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# Resolución a 4096

vrx.width(ADC.WIDTH_12BIT) # resoolución de salida 4096
vry.width(ADC.WIDTH_12BIT)    

servo = PWM(Pin(25), freq=50)

while True:
    
    
    valorx=vrx.read()  #Lee el valor de resistencia del eje x der joystck
    #print("bitx:" , valorx) # Para ver el valor de x
    #utime.sleep_ms(2000)
    
    if valorx >= 4080:  # Condiciones para el Eje X de 0 a 4096
        print ("derecha")
        utime.sleep_ms(2000)
        servo.duty(4095)
    if valorx <=200:
        print ("izquierda")
        utime.sleep_ms(2000)
    
    valory=vry.read()  # Lee el valor de resistencia del eje y der joystck
    #print("bity:" , valory) # si desea leer el valor sólo de y
    #utime.sleep_ms(2000) #2 segundos
    
    if valory <= 40 : # El eje Y el valor varia entre 0 y 4096
        print("arriba")
        utime.sleep_ms(200)        
    if valory >= 4000:
        print("abajo")
        utime.sleep_ms(200)
    
    valorsw=sw.read()
    if valorsw <= 0:
        print ("click")
        led.value(1)  #enciende el led
        utime.sleep_ms(100)
    else:
        led.value(0)  #apaga el led
        utime.sleep_ms(100)
    #print("Valores: Pulsador {} , eje x: {}, eje y: {}".format(valorsw,valorx,valory)) # imprime los tres valores
    utime.sleep_ms(2000)
    

    
          