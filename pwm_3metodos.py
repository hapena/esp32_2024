from machine import Pin, ADC, PWM
from utime import sleep_ms, sleep_us

led = PWM(Pin(4), freq=50)

while True:
    
    for i in range(25, 125):
        led.duty(i)
        sleep_ms(1)
    print("duty")
    
    
    
    