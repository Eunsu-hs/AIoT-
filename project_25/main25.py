import requests
import re

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=fFWLxGIoKo8cQCIuS5Is1fVoiKXkdls%2FU5DSGRwzmbiwIBI0nlz5V6jllexlrGLKR9y8wV3E3i0SMPTLtAhyvw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
response = requests.get(url)

pm10 = re.findall(r'<pm10Value>(.+)</pm10Value>',response.text)
pm25 = re.findall(r'<pm25Value>(.+)</pm25Value>',response.text)
stationName = re.findall(r'<stationName>(.+)</stationName>',response.text)

print(pm10)
print(pm25)
print(stationName)