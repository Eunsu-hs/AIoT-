import time
import datetime
import os

def speak(option, msg) :
    os.system("espeak {} '{}'".format(option,msg))

try:
    while True:
        now = datetime.datetime.now()
        nowSec = now.second
        
        if nowSec == 0:
            nowTime = now.strftime('   현재 시간은 %H시 %M분 입니다')
            print(nowTime)
            
            option = '-s 180 -p 50 -a 200 -v ko+f5'
            msg = nowTime
            speak(option,msg)
            
        time.sleep(1)

except KeyboardInterrupt:
    pass