from gpiozero import Button
import time

sw1 = Button(14)
sw2 = Button(15)
sw3 = Button(18)
sw4 = Button(23)
sw5 = Button(24)

try:
    while 1:
        if sw1.is_pressed:
            print("sw1")
        elif sw2.is_pressed:
            print("sw2")
        elif sw3.is_pressed:
            print("sw3")
        elif sw4.is_pressed:
            print("sw4")
        elif sw5.is_pressed:
            print("sw5")
        else:
            pass
        
        time.sleep(0.1)
    
except KeyboardInterrupt:
    pass