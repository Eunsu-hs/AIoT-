import os
 
def speak(option, msg) :
    os.system("espeak {} '{}'".format(option,msg))
    
option = '-s 180 -p 50 -a 200 -v ko+f5'
msg = '   안녕하세요 라즈베리파이 40개 프로젝트 입니다.'
 
print('espeak', option, msg)
speak(option,msg)