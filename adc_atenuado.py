print("Hello, ESP32!")
from machine import Pin, ADC
from utime import sleep_ms

pot = ADC(Pin(36))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)

ldr = ADC(Pin(39))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_10BIT)


while True:
    
    lec_pot = pot.read()
    lec_ldr = ldr.read()
    print(lec_pot," ", lec_ldr)
    sleep_ms(100)