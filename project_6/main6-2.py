from gpiozero import DigitalInputDevice #gpiozero 라이브러리에서 DigitalInputDevice클래스를 가져옵니다. 
from gpiozero import OutputDevice #gpiozero 라이브러리에서 OutputDevice클래스를 가져옵니다. 
import time # time 라이브러리를 가져옵니다.

bz = OutputDevice(18)#gpio 18번 핀을 부저 제어 핀으로 초기화
gas = DigitalInputDevice(17)#gpio 17번 핀을 MQ2 센서 입력 핀으로 초기화

try: 
    while True: #무한루프문으로 아래 동작을 반복합니다.
        if gas.value == 0:    # ←DO핀이 LOW(0)이면 가스가 감지된 것으로 판단합니다
            print("가스 감지됨") #터미널에 '가스 감지됨' 출력
            bz.on() #부저 on
        else:                 # ←DO핀이 HIGH(1)이면 정상 상태로 판단합니다
            print("정상")   #터미널에 '정상' 출력
            bz.off() #부저 off

        time.sleep(0.2) #0.2초 마다 센서값을 반복 확인합니다.

except KeyboardInterrupt:#키보드 인터럽트 발생시 무한루프문을 종료합니다(Ctrl+c)
    pass

bz.off()#프로그램 종료 시 부저를 OFF처리합니다.
