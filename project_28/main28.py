import urllib.request # 웹 요청 라이브러리
import json # JSON 데이터 처리 라이브러리

api_key = 'Enter your API key here' # OpenWeatherMap API 키

url = f"https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid={api_key}&units=metric&lang=en&cnt=8" # 서울 24시간 예보 URL

with urllib.request.urlopen(url) as r: # API에 요청 보내기
data = json.loads(r.read()) # 응답을 JSON으로 변환

time = [(int(item['dt_txt'][11:13]) + 9) % 24 for item in data['list’]] # 시간 목록 추출 (UTC+9 KST(한국시간) 변환)
temp = [item['main']['temp'] for item in data['list']] # 기온 목록 추출
humi = [item['main']['humidity'] for item in data['list']] # 습도 목록 추출
desc = [item['weather'][0]['description'] for item in data['list']] # 날씨 설명 목록 추출

print(time) # 시간 출력
print(temp) # 기온 출력
print(humi) # 습도 출력
print(desc) # 날씨 설명 출력
