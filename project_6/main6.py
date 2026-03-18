from gpiozero import MCP3208
import time

gas = MCP3208(channel=0)

try:
    while 1:
        gasValue = gas.value * 100
        print(gasValue)

        time.sleep(0.2)


except KeyboardInterrupt:
    pass
