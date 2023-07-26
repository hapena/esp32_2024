from machine import Pin, PWM
import utime

red = PWM(Pin(2), freq=10000)
green = PWM(Pin(4), freq=10000)
blue = PWM(Pin(5), freq=10000)


while True:
    
    red.duty(35)  # 0 y 1023-------  0 y 255
    green.duty(74)
    blue.duty(90)
    
    