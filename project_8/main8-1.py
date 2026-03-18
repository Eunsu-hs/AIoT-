from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=20, trigger=16)

try:
    while True:
        distanceCm = sensor.distance * 100
        if (distanceCm >=0) and (distanceCm<10):
            print("do")
        elif (distanceCm >=10) and (distanceCm<13):
            print("le")
        elif (distanceCm >=13) and (distanceCm<16):
            print("mi")
        elif (distanceCm >=16) and (distanceCm<19):
            print("fa")
        elif (distanceCm >=19) and (distanceCm<22):
            print("sol")
        elif (distanceCm >=22) and (distanceCm<25):
            print("la")
        elif (distanceCm >=25) and (distanceCm<28):
            print("si")
        elif (distanceCm >=28) and (distanceCm<31):
            print("5oc do")
        else:
            print("no")
        
        print("cm:",distanceCm)
        sleep(0.5)
    
except KeyboardInterrupt:
    pass