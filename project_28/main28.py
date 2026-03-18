import requests
import re

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"
response = requests.get(url)

time = re.findall(r'<hour>(.+?)</hour>',response.text)
temp = re.findall(r'<temp>(.+)</temp>',response.text)
humi = re.findall(r'<reh>(.+?)</reh>',response.text)
wfKor = re.findall(r'<wfKor>(.+?)</wfKor>',response.text)

print(time)
print(temp)
print(humi)
print(wfKor)