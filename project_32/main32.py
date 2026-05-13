import speech_recognition as sr # 음성 인식 라이브러리 임포트

try:
    while True: # 키보드 인터럽트(Ctrl+C)가 발생할 때까지 무한 반복
        
        r = sr.Recognizer() # 음성 인식기 객체 생성
        
        with sr.Microphone() as source: # 기본 마이크를 입력 소스로 사용
            print("Say something!") # 사용자에게 말하도록 안내 메시지 출력
            audio = r.listen(source) # 마이크에서 음성을 녹음하여 audio에 저장
        
        try:
            text = r.recognize_google(audio, language='ko-KR') # 녹음된 음성을 한국어로 텍스트 변환
            print("You said: " + text) # 인식된 텍스트 출력
            
            if text in "날씨": # text가 "날씨" 문자열 안에 포함되는지 확인
                print("날씨 음성을 인식하였습니다.") # 날씨 관련 음성 인식 성공 메시지 출력
        
        except sr.UnknownValueError: # 음성은 감지됐지만 내용을 인식하지 못한 경우
            print("Google Speech Recognition could not understand audio") # 인식 실패 메시지 출력
        
        except sr.RequestError as e: # Google API 서버 요청 자체가 실패한 경우
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) # 오류 내용 출력

except KeyboardInterrupt: # Ctrl+C 입력 시 프로그램 정상 종료
    pass # 아무 처리 없이 루프 탈출
