from machine import Pin, PWM, ADC
from utime import sleep



led = PWM(Pin(15), freq=60000)
potenciometro = ADC(Pin(36))     

while True:
    
    duty_cycle = potenciometro.read_u16()
    led.duty(duty_cycle)
    print(duty_cycle)
    sleep(0.005)
    
    
    
  
        
        
        
      
if __name__ == '__main__':
    main()