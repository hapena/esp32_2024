from machine import Pin, ADC, PWM
from utime import sleep_ms, sleep_us

led = PWM(Pin(13), freq=10000)

while True:
    
    for i in range(0, 1023):
        led.duty(i)
        sleep_ms(1)
    print("duty")
    
    
    
   
    
    