from gpiozero import LED #'gpiozero' 라이브러리에서 'LED'클래스를 가져옵니다.
from time import sleep #'time' 라이브러리에서 'sleep' 함수를 가져옵니다.

carLedRed = 2 #다양한 LED 핀의 핀 번호를 변수로 정의합니다 (Lines 4~8)
carLedYellow = 3    #carLedRed, carLedYellow, carLedGreen, humanLedRed,humanLedGreen 변수에 각각 핀 번호를 할당합니다
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21
# 각 LED를 LED 클래스의 객체로 초기화하며, 핀 번호를 사용하여 LED 객체를 생성합니다 (Lines 10 ~ 14)
carLedRed = LED(2) # 자동차 신호등 - 빨간불 (GPIO 2)
carLedYellow = LED(3)# 자동차 신호등 - 노란불 (GPIO 3)
carLedGreen = LED(4)# 자동차 신호등 - 초록불 (GPIO 4)
humanLedRed = LED(20)# 보행자 신호등 - 빨간불 (GPIO 20)
humanLedGreen = LED(21)# 보행자 신호등 - 초록불 (GPIO 21)

try: # 무한 루프 （while 1:’）를 시작, 이 루프에서는 아래의 동작을 반복합니다 (Lines 16 ~ 35)
    while 1:# 무한 반복 (신호등 계속 순환)
        carLedRed.value = 0# 자동차 초록불 / 보행자 빨간불
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(3.0)# 3초 유지
        carLedRed.value = 0# 자동차 노란불 / 보행자 빨간불 유지
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)# 1초 유지
        carLedRed.value = 1# 자동차 빨간불 / 보행자 초록불
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)# 3초 유지
    
except KeyboardInterrupt: # 사용자가 Ctrl + C를 누를 때까지 코드를 실행하는 예외 처리 블록입니다.
    pass # 사용자가 Ctrl + C를 누르면 루프가 중단되고 코드 실행이 종료됩니다

carLedRed.value = 0 # 코드 실행이 종료되면 모든 LED를 꺼줍니다(Lines 40 ~ 44)
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0