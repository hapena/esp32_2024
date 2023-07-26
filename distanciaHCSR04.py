from hcsr04 import HCSR04
from time import sleep


medidor = HCSR04 (trigger_pin = 4, echo_pin = 5)
while (True):
    try:
        distancia = medidor.distance_cm ()
        print ("Distancia = ", distancia)
        sleep (1)
    except:
        print ("Error!")