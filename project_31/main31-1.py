import speech_recognition as sr # 음성 인식 라이브러리 임포트
from gpiozero import LED # Raspberry Pi GPIO 제어를 위한 LED 클래스 임포트

greenLed = LED(16) # GPIO 16번 핀에 연결된 초록색 LED 객체 생성
blueLed = LED(20) # GPIO 20번 핀에 연결된 파란색 LED 객체 생성
redLed = LED(21) # GPIO 21번 핀에 연결된 빨간색 LED 객체 생성

try:
    while True: # 키보드 인터럽트(Ctrl+C)가 발생할 때까지 무한 반복
        
        # Record Audio
        r = sr.Recognizer() # 음성 인식기 객체 생성
        
        with sr.Microphone() as source: # 기본 마이크를 입력 소스로 사용
            print("Say something!") # 사용자에게 말하도록 안내 메시지 출력
            audio = r.listen(source) # 마이크에서 음성을 녹음하여 audio에 저장
        
        # Speech recognition using Google Speech Recognition
        try:
            text = r.recognize_google(audio, language='ko-KR') # 녹음된 음성을 한국어로 텍스트 변환
            print("You said: " + text) # 인식된 텍스트 출력
            
            if text in "빨간색": # text가 "빨간색" 문자열 안에 포함되는지 확인
                greenLed.value = 0 # 초록 LED 끄기
                blueLed.value = 0 # 파란 LED 끄기
                redLed.value = 1 # 빨간 LED 켜기
            
            elif text in "파란색": # text가 "파란색" 문자열 안에 포함되는지 확인
                greenLed.value = 0 # 초록 LED 끄기
                blueLed.value = 1 # 파란 LED 켜기
                redLed.value = 0 # 빨간 LED 끄기
            
            elif text in "녹색": # text가 "녹색" 문자열 안에 포함되는지 확인
                greenLed.value = 1 # 초록 LED 켜기
                blueLed.value = 0 # 파란 LED 끄기
                redLed.value = 0 # 빨간 LED 끄기
            
            elif text in "꺼": # text가 "꺼" 문자열 안에 포함되는지 확인
                greenLed.value = 0 # 초록 LED 끄기
                blueLed.value = 0 # 파란 LED 끄기
                redLed.value = 0 # 빨간 LED 끄기
        
        except sr.UnknownValueError: # 음성은 감지됐지만 내용을 인식하지 못한 경우
            print("Google Speech Recognition could not understand audio") # 인식 실패 메시지 출력
        
        except sr.RequestError as e: # Google API 서버 요청 자체가 실패한 경우
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) # 오류 내용 출력

except KeyboardInterrupt: # Ctrl+C 입력 시 프로그램 정상 종료
    pass # 아무 처리 없이 루프 탈출

GPIO.cleanup() # GPIO 핀 설정을 초기화하여 자원 해제
