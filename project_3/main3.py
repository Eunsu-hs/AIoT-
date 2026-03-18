from gpiozero import Button
from gpiozero import LED
from time import sleep

ledRed = LED(23)
ledBlue = LED(24)
swPin = Button(21)

try:
    while 1:
        swValue = swPin.is_pressed
        print(swValue)
        sleep(0.1)
    
except KeyboardInterrupt:
    pass
