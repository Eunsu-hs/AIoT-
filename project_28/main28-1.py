import requests
import re

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"
response = requests.get(url)

time = re.findall(r'<hour>(.+?)</hour>',response.text)
temp = re.findall(r'<temp>(.+)</temp>',response.text)
humi = re.findall(r'<reh>(.+?)</reh>',response.text)
wfKor = re.findall(r'<wfKor>(.+?)</wfKor>',response.text)
text = ""
for i in range(8):
    text = text + "(" + str(time[i]) + "시 "
    text = text + str(temp[i]) + "C "
    text = text + str(humi[i]) + "% "
    text = text + str(wfKor[i]) + ")"
    
print(text)