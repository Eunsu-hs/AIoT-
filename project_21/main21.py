import os
import time

try:
    while True:
        temp = os.popen("vcgencmd measure_temp").readline()
        print(temp)
        time.sleep(1.0)
    
except KeyboardInterrupt:
    pass
