from gpiozero import LED
import time

carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    while 1:
        carLedRed.off()
        carLedYellow.off()
        carLedGreen.on()
        humanLedRed.on()
        humanLedGreen.off()
        time.sleep(5.0)
        
        carLedRed.off()
        carLedYellow.on()
        carLedGreen.off()
        humanLedRed.on()
        humanLedGreen.off()
        time.sleep(5.0)
        
        carLedRed.on()
        carLedYellow.off()
        carLedGreen.off()
        humanLedRed.off()
        humanLedGreen.on()
        time.sleep(5.0)
    
except KeyboardInterrupt:
    pass