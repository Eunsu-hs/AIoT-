import serial
from gpiozero import LED

bleSerial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)

try:
    while True:
        data = bleSerial.readline()
        data = data.decode()
        if data.find("green_on") >= 0 :
            print("ok green on")
            greenLed.on()
        elif data.find("green_off") >= 0 :
            print("ok green off")
            greenLed.off()
        elif data.find("blue_on") >= 0 :
            print("ok blue on")
            blueLed.on()
        elif data.find("blue_off") >= 0 :
            print("ok blue off")
            blueLed.off()
        elif data.find("red_on") >= 0 :
            print("ok red on")
            redLed.on()
        elif data.find("red_off") >= 0 :
            print("ok red off")
            redLed.off()
        
except KeyboardInterrupt:
    pass

bleSerial.close()
