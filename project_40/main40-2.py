import cv2
import os

try:
    os.makedirs("images", exist_ok=True)
    os.makedirs("images/1", exist_ok=True)
    os.makedirs("images/2", exist_ok=True)
    os.makedirs("images/3", exist_ok=True)
    os.makedirs("images/4", exist_ok=True)
except:
    pass

cap = cv2.VideoCapture(-1)

img1_cnt = 0
img2_cnt = 0
img3_cnt = 0
img4_cnt = 0
while True:
    ret, frame = cap.read()

    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('1'):
        print('1 ok')
        cv2.imwrite(f"images/1/{img1_cnt}.png", frame)
        img1_cnt = img1_cnt + 1
    elif key == ord('2'):
        print('2 ok')
        cv2.imwrite(f"images/2/{img2_cnt}.png", frame)
        img2_cnt = img2_cnt + 1
    elif key == ord('3'):
        print('3 ok')
        cv2.imwrite(f"images/3/{img3_cnt}.png", frame)
        img3_cnt = img3_cnt + 1
    elif key == ord('4'):
        print('4 ok')
        cv2.imwrite(f"images/4/{img4_cnt}.png", frame)
        img4_cnt = img4_cnt + 1

cap.release()
cv2.destroyAllWindows()