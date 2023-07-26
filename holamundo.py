from machine import Pin
import utime

led_onboard = Pin(2, Pin.OUT)


while True:
    led_onboard.value(1)
    print("on")
    utime.sleep(0.3)
    led_onboard.value(0)
    print("off")
    utime.sleep(0.3)
    


if __name__==("__main__"):
    main()



