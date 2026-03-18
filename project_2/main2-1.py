from gpiozero import LEDBoard# ‘gpiozero’ 라이브러리에서 ‘LEDBoard’ 클래스를 가져옵니다
from time import sleep# ‘time’ 라이브러리에서 ‘sleep’ 함수를 가져옵니다

leds = LEDBoard(2,3,4,20,21)# LEDBoard 클래스를 사용하여 다수의 LED를 초기화합니다 (하나의 객체로 관리)
# 여기서는 핀 번호 2, 3, 4, 20, 21을 가진 다섯 개의 LED를 초기화합니다
try:# 무한 루프 ‘while 1:’ 시작되며, 이 루프에서는 아래의 동작을 반복합니다 (Lines 06 ~ 14)
    while 1:
        leds.value = (0,0,1,1,0)# 자동차: 초록불 ON / 보행자: 빨간불 ON
        sleep(3.0)# 3초 동안 유지
        leds.value = (0,1,0,1,0) # 자동차: 노란불 ON / 보행자: 빨간불 유지
        sleep(1.0)# 1초 동안 유지
        leds.value = (1,0,0,0,1) # 자동차: 빨간불 ON / 보행자: 초록불 ON
        sleep(3.0)# 3초 동안 유지
    
except KeyboardInterrupt:# 사용자가 Ctrl + C를 누를 때까지 코드를 실행하는 예외 처리 블록입니다.
    pass # 사용자가 Ctrl + C를 누르면 루프가 중단되고 코드 실행이 종료됩니다

leds.off()# 코드 실행이 종료되면 모든 LED를 꺼줍니다
