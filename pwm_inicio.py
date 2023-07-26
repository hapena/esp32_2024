from machine import Pin, PWM
import utime


led = PWM(Pin(15), freq = 50)

while True:
    
    for ciclo_trabajo in range(0, 1024):
        led.duty(ciclo_trabajo)
        utime.sleep_ms(5)
        
        
        