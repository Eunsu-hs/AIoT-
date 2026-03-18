import requests
import re
import os
import time

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"

def speak(option, msg) :
    os.system("espeak {} '{}'".format(option,msg))
    
try:
    while 1:
        response = requests.get(url)
        temp = re.findall(r'<temp>(.+)</temp>',response.text)
        humi = re.findall(r'<reh>(.+)</reh>',response.text)
        
        msg = '    기온은 ' + temp[0].split('.')[0] + '도 습도는 ' + humi[0] + '퍼센트 입니다'
        print(msg)
        option = '-s 180 -p 50 -a 200 -v ko+f5'
        speak(option,msg)
        time.sleep(10.0)
        
except KeyboardInterrupt:
    pass