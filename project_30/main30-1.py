import paho.mqtt.client as mqtt   # MQTT 통신 모듈 불러오기
import time                       # 시간 관련 기능 모듈 불러오기
from gpiozero import LED          # GPIO 제어 모듈에서 LED 클래스 불러오기
import threading                  # 두 작업을 동시에 처리하기 위한 스레드 모듈 불러오기

# LED 설정
greenLed = LED(16)   # 16번 GPIO 핀 초록 LED
blueLed = LED(20)    # 20번 GPIO 핀 파란 LED
redLed = LED(21)     # 21번 GPIO 핀 빨간 LED


# 메시지 수신 시 실행되는 함수
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))  
    # 수신된 토픽 이름과 바이트 데이터 출력

    message = msg.payload.decode()  
    # 바이트 데이터를 문자열로 변환

    print(message)

    if message == "green_on":
        greenLed.on()

    elif message == "green_off":
        greenLed.off()

    elif message == "blue_on":
        blueLed.on()

    elif message == "blue_off":
        blueLed.off()

    elif message == "red_on":
        redLed.on()

    elif message == "red_off":
        redLed.off()


# MQTT 클라이언트 생성
client = mqtt.Client()

# 메시지 수신 함수 연결
client.on_message = on_message

# 브로커 IP 주소 설정
broker_address = "192.168.137.230"

# 브로커 연결
client.connect(broker_address)

# "led" 토픽 구독
client.subscribe("led", 1)


# 발행할 숫자 초기값
count = 0


# 메시지 발행 스레드 함수
def send_thread():
    global count

    while True:
        count = count + 1
        client.publish("hello", str(count))
        print("발행된 메시지:", count)

        time.sleep(1.0)


# 스레드 생성 및 시작
task = threading.Thread(target=send_thread)
task.start()


# 메시지 수신 대기
client.loop_forever()
