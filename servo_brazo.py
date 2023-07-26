from machine import Pin, PWM
import utime

def main():
    
    servo_mano = PWM(Pin(27), freq = 50)        
    servo_codo = PWM(Pin(14), freq = 50)
    servo_brazo = PWM(Pin(12), freq = 50)
    
    def map(x):
        return int((x - 0) * (130- 34) / (180 - 0) + 34)
    
    while True:
        angulo = float(input('Ingrese un ángulo de la mano: '))
        if angulo >= 0 and angulo <= 180:
            m = map(angulo)
            servo_mano.duty(m)
            print(m)
            
        else:
            print('Digite un ángulo entre 0 y 180')
        
        angulo = float(input('Ingrese un ángulo del codo: '))
        
        
        if angulo >= 0 and angulo <= 180:
            m = map(angulo)
            servo_codo.duty(m)
            print(m)    
            
        else:
            print('Digite un ángulo entre 0 y 180')
            
         
            
        
    
if __name__ == '__main__':
    main()