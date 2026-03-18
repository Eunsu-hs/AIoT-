from gpiozero import LED
import time
import requests
import re

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)

try:
    while True:
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=fFWLxGIoKo8cQCIuS5Is1fVoiKXkdls%2FU5DSGRwzmbiwIBI0nlz5V6jllexlrGLKR9y8wV3E3i0SMPTLtAhyvw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
        response = requests.get(url)
        
        pm10 = re.findall(r'<pm10Value>(.+)</pm10Value>',response.text)
        pm25 = re.findall(r'<pm25Value>(.+)</pm25Value>',response.text)
        stationName = re.findall(r'<stationName>(.+)</stationName>',response.text)

        findNum = stationName.index('강남구')
        print("pm10:",pm10[findNum])
        print("pm25:",pm25[findNum])
        print("station:",stationName[findNum])
        
        pm25 = int(pm25[findNum])
        if pm25 <= 30:
            greenLed.on()
            blueLed.off()
            redLed.off()
        elif pm25 >= 31 and pm25 <= 80:
            greenLed.off()
            blueLed.on()
            redLed.off()
        elif pm25 >= 81 and pm25 <= 150:
            greenLed.off()
            blueLed.off()
            redLed.on()
        elif pm25 >= 151:
            greenLed.on()
            blueLed.on()
            redLed.on()
            
        for i in range(60):
            time.sleep(60000)
    
except KeyboardInterrupt:
    pass

greenLed.off()
blueLed.off()
redLed.off()




