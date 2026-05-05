import paho.mqtt.client as mqtt   # MQTT 통신 모듈 불러오기
import time                       # 시간 관련 기능 모듈 불러오기
from gpiozero import LED          # GPIO 제어 모듈에서 LED 클래스 불러오기

# LED 핀 설정
greenLed = LED(16)   # 16번 핀에 연결된 초록 LED
blueLed = LED(20)    # 20번 핀에 연결된 파란 LED
redLed = LED(21)     # 21번 핀에 연결된 빨간 LED


# 메시지 수신 시 실행되는 함수
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))  # 수신된 토픽과 데이터 출력
    
    message = msg.payload.decode()  # 바이트 데이터를 문자열로 변환
    print(message)

    if message == "green_on":
        greenLed.on()   # 초록 LED 켜기

    elif message == "green_off":
        greenLed.off()  # 초록 LED 끄기

    elif message == "blue_on":
        blueLed.on()    # 파란 LED 켜기

    elif message == "blue_off":
        blueLed.off()   # 파란 LED 끄기

    elif message == "red_on":
        redLed.on()     # 빨간 LED 켜기

    elif message == "red_off":
        redLed.off()    # 빨간 LED 끄기


# MQTT 클라이언트 생성
client = mqtt.Client()

# 메시지 수신 함수 연결
client.on_message = on_message

# 브로커 IP 주소 설정
broker_address = "192.168.137.230"

# 브로커 연결
client.connect(broker_address)

# "led" 토픽 구독 (QoS 1)
client.subscribe("led", 1)

# 무한 루프 실행 (메시지 대기)
client.loop_forever()
