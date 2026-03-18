from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=20, trigger=16)
try:
    while True:
        distanceCm = sensor.distance * 100
        print('cm: ', distanceCm)
        sleep(0.5)

except KeyboardInterrupt:
    pass
