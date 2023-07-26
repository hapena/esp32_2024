from machine import Pin, PWM
import utime

def main():
    
    servo = PWM(Pin(15), freq=50)
    
    def map(x):
        return int((x - 0) * (130-34) / (180 - 0) + 34)
    
    while True:
        
         
        angulo = float(input("ingrese el angulo entre 0° y 180°: "))
         
        if angulo >= 0 and angulo <= 180:
            
            m = map(angulo)
            servo.duty(m)
            print("angulo", angulo, "resolucion", m)
        
        else:
                     
            print("Digite un angulo entre 0 y 180")
             

if __name__=="__main__":
    main()
             
             
    
    
