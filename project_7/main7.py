from gpiozero import TonalBuzzer
import time

piezo = TonalBuzzer(21)

try:
    while True:
        piezo.play(261.6)
        time.sleep(1.0)
        piezo.play(293.6)
        time.sleep(1.0)
        piezo.play(329.6)
        time.sleep(1.0)
        piezo.play(349.2)
        time.sleep(1.0)
        piezo.play(391.9)
        time.sleep(1.0)
        piezo.stop()
        time.sleep(1.0)

except KeyboardInterrupt:
    pass