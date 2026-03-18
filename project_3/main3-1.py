from gpiozero import Button
from gpiozero import LED
from time import sleep

ledRed = LED(23)
ledBlue = LED(24)
swPin = Button(21)

swState = 0

try:
    while 1:
        swValue = swPin.is_pressed
        if swValue == True:
            if swState == 0:
                swState = 1
            else:
                swState = 0
            sleep(0.5)
            
        print(swState)
        sleep(0.1)
    
except KeyboardInterrupt:
    pass

