from gpiozero import Buzzer,MCP3208
import time

bz = Buzzer(18)
gas = MCP3208(channel=0)

try:
    while 1:
        gasValue = gas.value * 100
        print(gasValue)
        if gasValue >= 10:
            bz.on()
        else:
            bz.off()

        time.sleep(0.2)


except KeyboardInterrupt:
    pass

bz.off()