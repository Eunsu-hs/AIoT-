import requests

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"
response = requests.get(url)

print(response.text)