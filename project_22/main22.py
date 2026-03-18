from gpiozero import Motor
import time

motor = Motor(21, 20)

try:
    while 1:
        motor.stop()
        print("0")
        time.sleep(5.0)
        
        motor.forward(0.5)
        print("50")
        time.sleep(5.0)
        
        motor.forward(1.0)
        print("100")
        time.sleep(5.0)
        
except KeyboardInterrupt:
    pass

motor.stop()