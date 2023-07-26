from machine import Pin, ADC
from utime import sleep_ms

sensor_adc = ADC(Pin(2))


while True:
    factor_con = 3.3/65535
    factor_dos = 400/65535
    lectura = sensor_adc.read_u16()
    voltaje = lectura*factor_con
    distancia = lectura*factor_dos
    print(lectura, voltaje, distancia)
    sleep_ms(100)
    
    


