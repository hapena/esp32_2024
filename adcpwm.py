from machine import Pin, ADC, PWM
from utime import sleep_ms

led = PWM(Pin(15), freq=10000)


pot = ADC(Pin(36))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)


while True:
    
    lec_pot = pot.read()
    led.duty(lec_pot)
    sleep_ms(50)