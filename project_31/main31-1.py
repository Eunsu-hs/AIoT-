import speech_recognition as sr
from gpiozero import LED

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)

try:
    while True :
        # Record Audio
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        # Speech recognition using Google Speech Recognition
        try:
            text = r.recognize_google(audio, language='ko-KR')
            print("You said: " + text)
            if text in "빨간색":
                greenLed.value = 0
                blueLed.value = 0
                redLed.value = 1
            elif text in "파란색":
                greenLed.value = 0
                blueLed.value = 1
                redLed.value = 0
            elif text in "녹색":
                greenLed.value = 1
                blueLed.value = 0
                redLed.value = 0
            elif text in "꺼":
                greenLed.value = 0
                blueLed.value = 0
                redLed.value = 0
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    pass

GPIO.cleanup()
