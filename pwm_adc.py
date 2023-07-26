from machine import Pin, PWM, ADC
import utime

led = PWM(Pin(15), freq = 50)

# calibrar.... de acuerdo a las especificaciones del sensor
sensor = ADC(Pin(39))
sensor.atten(ADC.ATTN_11DB)  # para calibrar de 0 a 3.6v
sensor.width(ADC.WIDTH_10BIT) # establecer resolucion de 10 bits hasta 1023


while True:
    
    ciclo_trabajo = sensor.read()
    print(ciclo_trabajo)
    led.duty(ciclo_trabajo)
    utime.sleep_ms(5)
    
