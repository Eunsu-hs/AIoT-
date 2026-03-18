from gpiozero import MotionSensor
import time

pirPin = MotionSensor(16)

try:
    while True:
        sensorValue = pirPin.value
        print(sensorValue)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
