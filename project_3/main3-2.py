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
            
        if swState == 1:
            ledRed.on()
            ledBlue.off()
            sleep(0.1)
            ledRed.off()
            ledBlue.on()
            sleep(0.1)
        else:
            ledRed.off()
            ledBlue.off()
    
except KeyboardInterrupt:
    pass

ledRed.off()
ledBlue.off()
