from machine import Pin, PWM
import utime

def main():
    
    servo = PWM(Pin(4), freq=50)
    
    def map(x):
        #return int((x - 0) * (8000-1800) / (180 - 0) +1800) # v1.19 -- duty_u16(m) -- 0 y 65536
        return int((x - 0) * (125- 25) / (180 - 0) + 25) # v1.19 -- duty(m) -- 0 y 1023
        #return int((x - 0) * (2400000- 500000) / (180 - 0) + 500000) # v1.19 --duty_ns() --0 y 1_000_000_000
        
    while True:
        
         
        angulo = float(input("ingrese el angulo entre 0° y 180°: "))
         
        if angulo >= 0 and angulo <= 180:
            
            m = map(angulo)
            #servo.duty_u16(m)
            servo.duty(m)
            #servo.duty_ns(m)
            print("angulo", angulo, "resolucion", m)
        
        else:
                     
            print("Digite un angulo entre 0 y 180")
             

if __name__=="__main__":
    main()
             
             
    
    

