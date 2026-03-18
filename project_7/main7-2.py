from gpiozero import Button,TonalBuzzer
import time

piezo = TonalBuzzer(21)

sw1 = Button(14)
sw2 = Button(15)
sw3 = Button(18)
sw4 = Button(23)
sw5 = Button(24)

try:
    while 1:
        if sw1.is_pressed:
            piezo.play(261.6)
        elif sw2.is_pressed:
            piezo.play(293.6)
        elif sw3.is_pressed:
            piezo.play(329.6)
        elif sw4.is_pressed:
            piezo.play(349.2)
        elif sw5.is_pressed:
            piezo.play(391.9)
        else:
            piezo.stop()
        
        time.sleep(0.1)
    
except KeyboardInterrupt:
    pass
