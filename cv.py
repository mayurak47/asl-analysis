import cv2
import os
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
top, right, bottom, left = 10, 350, 225, 590

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    cnt=0
    
    if not ret:
        break
    k = cv2.waitKey(1)
    
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 13:
        # ENTER pressed
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
        img_name = "opencv_frame_{}.png".format(img_counter)
        print("{} written!".format(img_name))
        path = '/Users/mayurarvind/'
        cv2.imwrite(os.path.join(path, img_name),res)
        img_counter += 1

cam.release()

cv2.destroyAllWindows()