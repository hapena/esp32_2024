from machine import Pin, PWM
from utime import sleep_ms

led = PWM(Pin(12), freq=5000)  

while True:
    
    for i in range(0,65000):
        led.duty_u16(i)
        sleep_ms(1)
          
  
    
    