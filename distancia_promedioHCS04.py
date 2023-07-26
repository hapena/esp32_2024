#Sensor de distancias HCS-R04
#Mapeo de GPIO de D1 Mini

D0 = 16
D1 = 5
D2 = 4
D3 = 0
D4 = 2
D5 = 14
D6 = 12
D7 = 13
D8 = 15

from hcsr04 import HCSR04
from time import sleep

medidor = HCSR04 (trigger_pin = D2 , echo_pin = D1)

def midePromedio ():
     suma=0
     for i in range (0,16):
         distancia = medidor.distance_cm ()
         sleep (0.1)
         if (distancia > 0):
             suma+=distancia
     return suma/16

while (True):
     print ("Distancia = ", midePromedio ())