from gpiozero import DistanceSensor,TonalBuzzer
from time import sleep

piezo = TonalBuzzer(21)

sensor = DistanceSensor(echo=20, trigger=16)

try:
    while True:
        distanceCm = sensor.distance * 100
        if (distanceCm >=0) and (distanceCm<10):
            print("do")
            piezo.play(261.6)
        elif (distanceCm >=10) and (distanceCm<13):
            print("le")
            piezo.play(293.6)
        elif (distanceCm >=13) and (distanceCm<16):
            print("mi")
            piezo.play(329.6)
        elif (distanceCm >=16) and (distanceCm<19):
            print("fa")
            piezo.play(349.2)
        elif (distanceCm >=19) and (distanceCm<22):
            print("sol")
            piezo.play(391.9)
        elif (distanceCm >=22) and (distanceCm<25):
            print("la")
            piezo.play(440.0)
        elif (distanceCm >=25) and (distanceCm<28):
            print("si")
            piezo.play(493.9)
        elif (distanceCm >=28) and (distanceCm<31):
            print("5oc do")
            piezo.play(523.0)
        else:
            print("no")
            piezo.stop()
        
        print("cm:",distanceCm)
        sleep(0.5)
    
except KeyboardInterrupt:
    pass
