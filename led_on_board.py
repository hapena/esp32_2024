from machine import Pin, ADC, PWM
from utime import  sleep, sleep_ms

led_a = Pin(19, Pin.OUT)
led_b = Pin(5, Pin.OUT)

while True:

    led_a.on()
    led_b.on()
    sleep_ms(1000)
    led_a.off()
    led_b.off()
    sleep_ms(1000)
    

