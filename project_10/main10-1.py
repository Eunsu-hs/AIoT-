import os
import glob
import time
from gpiozero import LED

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

try:
    while True : 
        temperature = read_temp()
        print(temperature)
        if temperature >= 30:
            greenLed.value = 0
            blueLed.value = 0
            redLed.value = 1
        elif 20 <= temperature < 30:
            greenLed.value = 1
            blueLed.value = 0
            redLed.value = 0
        elif temperature < 20:
            greenLed.value = 0
            blueLed.value = 1
            redLed.value = 0
        
        time.sleep(2.0)

except KeyboardInterrupt:
    pass
