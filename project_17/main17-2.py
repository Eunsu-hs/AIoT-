from gpiozero import LED
import time
import os

carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

def speak(option, msg) :
    os.system("espeak {} '{}'".format(option,msg))

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
        
        option = '-s 180 -p 50 -a 200 -v ko+f5'
        msg = '   녹색불 입니다. 건너가도 좋습니다.'
        speak(option,msg)
        time.sleep(5.0)
    
except KeyboardInterrupt:
    pass