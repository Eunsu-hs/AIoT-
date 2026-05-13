import speech_recognition as sr  # 음성 인식 라이브러리 임포트

try:
    while True:  # Ctrl+C가 발생할 때까지 무한 반복
        
        # 오디오 녹음 준비
        r = sr.Recognizer()  # Recognizer 객체 생성
        
        with sr.Microphone() as source:  # 기본 마이크 사용
            print("Say something!")  # 안내 메시지 출력
            audio = r.listen(source)  # 음성 입력 저장
        
        # Google 음성 인식을 사용하여 텍스트 변환
        try:
            # 한국어 음성 인식
            print(
                "You said: " +
                r.recognize_google(audio, language='ko-KR')
            )
        
        except sr.UnknownValueError:
            # 음성을 이해하지 못한 경우
            print("Google Speech Recognition could not understand audio")
        
        except sr.RequestError as e:
            # API 요청 실패
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e)
            )

except KeyboardInterrupt:
    # Ctrl+C 입력 시 프로그램 종료
    pass
