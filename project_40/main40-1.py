import cv2

cap = cv2.VideoCapture(-1)

while True:
    ret, frame = cap.read()

    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('1'):
        print('1 ok')
    elif key == ord('2'):
        print('2 ok')
    elif key == ord('3'):
        print('3 ok')
    elif key == ord('4'):
        print('4 ok')        

cap.release()
cv2.destroyAllWindows()