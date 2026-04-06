from gpiozero import MotionSensor #gpiozero 라이브러리에서 MotionSensor 클래스를 가져옵니다.
import time #time라이브러리를 가져옵니다.

pirPin = MotionSensor(16) #GPIO 16번 핀을 PIR 모션 센서 입력 핀으로 초기화합니다.

try:
    while True: #무한루프 시작
        sensorValue = pirPin.value #PIR센서의 현재 값을 읽어 변수에 저장합니다(감지시:1/미감지시:0)
        print(sensorValue) #센서 값을 터미널에 저장합니다.
        time.sleep(0.1) #0.1초마다 센서 값을 반복 확인합니다.

except KeyboardInterrupt: #키보드 인터럽트(Ctrl+c)발생 시 루프를 종료합니다.
    pass
