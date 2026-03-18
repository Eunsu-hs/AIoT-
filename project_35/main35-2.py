import cv2
from gpiozero import LED

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,320)
    camera.set(4,240)
        
    while(1):
        _, frame = camera.read()  

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = (100,100,120)
        upper_blue = (150,255,255)
        
        lower_green = (50, 150, 50)
        upper_green = (80, 255, 255)
        
        lower_red = (150, 50, 50)
        upper_red = (180, 255, 255)
                
        redMask = cv2.inRange(hsv, lower_red, upper_red)   
        greenMask = cv2.inRange(hsv, lower_green, upper_green)  
        blueMask = cv2.inRange(hsv, lower_blue, upper_blue)  

        redPixels = cv2.countNonZero(redMask)
        greenPixels = cv2.countNonZero(greenMask)
        bluePixels = cv2.countNonZero(blueMask)
        
        #print(redPixels,greenPixels,bluePixels)
        
        colorList = [redPixels,greenPixels,bluePixels]
        maxValue = max(colorList)
        maxPos = colorList.index(maxValue)
        print( maxValue, maxPos)
        
        if maxValue >= 500:
            if maxPos == 0: #red
                print("red on")
                greenLed.value = 0
                blueLed.value = 0
                redLed.value = 1
            elif maxPos == 1: #green
                print("green")
                greenLed.value = 1
                blueLed.value = 0
                redLed.value = 0
            elif maxPos == 2: #blue
                print("blue")
                greenLed.value = 0
                blueLed.value = 1
                redLed.value = 0
        else:
            greenLed.value = 0
            blueLed.value = 0
            redLed.value = 0
            
        cv2.imshow('frame',frame)
                 
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    greenLed.value = 0
    blueLed.value = 0
    redLed.value = 0

if __name__ == '__main__':
    main()


