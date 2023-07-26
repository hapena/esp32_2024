from machine import Pin, PWM
from utime import sleep_ms

  
servo = PWM(Pin(4), freq=50)

while True:

  for angulo in range(1800,8000):
    servo.duty_u16(angulo) 
    sleep_ms(50)