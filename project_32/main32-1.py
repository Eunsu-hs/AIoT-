import requests # HTTP 요청을 보내기 위한 라이브러리 임포트
import os # 운영체제 명령어 실행을 위한 라이브러리 임포트
import time # 시간 지연 처리를 위한 라이브러리 임포트

API_KEY = "Enter your API key here" # OpenWeatherMap API 키 설정
url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric" # 서울 날씨 요청 URL (단위: 섭씨)

def speak(option, msg): # 텍스트를 음성으로 출력하는 함수 정의
    os.system("espeak {} '{}'".format(option, msg)) # espeak 명령어로 option 설정과 함께 msg를 음성 출력

try:
    while 1: # 키보드 인터럽트(Ctrl+C)가 발생할 때까지 무한 반복
        
        response = requests.get(url) # 날씨 API에 GET 요청을 보내 응답 수신
        data = response.json() # 응답 데이터를 JSON 형식으로 파싱
        
        temp = data["main"]["temp"] # JSON 데이터에서 현재 기온(섭씨) 추출
        humi = data["main"]["humidity"] # JSON 데이터에서 현재 습도(%) 추출
        
        msg = ' 기온은 ' + str(int(temp)) + ' 도 습도는 ' + str(humi) + '퍼센트 입니다.' # 기온과 습도를 포함한 안내 문자열 생성
        
        print(msg) # 생성된 날씨 메시지 콘솔에 출력
        
        option = '-s 180 -p 50 -a 200 -v ko+f5' # espeak 옵션 설정 (속도 180, 음높이 50, 음량 200, 한국어 여성 음성)
        
        speak(option, msg) # 설정된 옵션과 메시지로 음성 출력 함수 호출
        
        time.sleep(10.0) # 10초 대기 후 다음 날씨 정보 요청

except KeyboardInterrupt: # Ctrl+C 입력 시 프로그램 정상 종료
    pass # 아무 처리 없이 루프 탈출
