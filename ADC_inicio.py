from machine import Pin, ADC
import utime


# Indicadores
led_rojo= Pin(15, Pin.OUT)
led_verde = Pin(2, Pin.OUT)

# calibrar.... de acuerdo a las especificaciones del sensor
sensor = ADC(Pin(39))
sensor.atten(ADC.ATTN_11DB)  # para calibrar de 0 a 3.6v
sensor.width(ADC.WIDTH_12BIT) # establecer resolucion de 12 bits hasta 4096

# sensor tem 0 y 100 grados
while True:
    
    lectura =  sensor.read()
    factor_de_conversion = 400/4096
    factor_dos = 3.3/4096
    distancia = factor_de_conversion * lectura
    voltaje = factor_dos * lectura
    print("D: ",distancia, "cm", " V", voltaje, "v", "Res", lectura, "b")
    utime.sleep_ms(100)
    
    if distancia < 20:
        
        led_rojo.value(1)
        led_verde.value(0)
        
        
    else:
        led_rojo.value(0)
        led_verde.value(1)
        
    

   



