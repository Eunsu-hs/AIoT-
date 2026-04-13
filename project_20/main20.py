from flask import Flask #웹 서버를 만드는 flask 라이브러리입니다
from gpiozero import LED #라즈베리 파이 GPIO핀 제어 라이브러리입니다
   
app = Flask(__name__) #Flask 앱을 생성합니다

red_led = LED(21)   #21번 핀에 연결된 led를 설정합니다

@app.route('/') #기본 주소 (/) 접속 시 실행
def flask():
   return "hello Flask" #브라우저에 텍스트를 출력합니다

@app.route('/ledon') #/ledon 주소 접속시 실행합니다
def ledOn():
   red_led.on()    #led켜기
   return "<h1> LED ON </h1> " #브라우저에 결과를 출력합니다

@app.route('/ledoff') #/ledoff 주소 접속 시 실행합니다
def LedOff():
   red_led.off()      #led끄기
   return "<h1> LED OFF </h1>" #브라우저에 결과를 출력합니다

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = "80") #모든 ip(0,0,0,0)에서 80번 포트로 서버를 실행합니다
