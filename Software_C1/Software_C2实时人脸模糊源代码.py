import cv2
import numpy as np

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')#opencv自带人脸模型

cap=cv2.VideoCapture(0)#打开摄像头，0指默认摄像头

while True:
    ret,img=cap.read()#读取一帧画面
    if not ret:
        break
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
    faces=face_detector.detectMultiScale(gray,1.3,5)#检测人脸
    for (x,y,w,h) in faces:
        face=img[y:y+h,x:x+w]#截取人脸区域
        img[y:y+h,x:x+w]=cv2.GaussianBlur(face,(25,25),0)#高斯模糊

    cv2.imshow('img',img)
    key = cv2.waitKey(1)#esc退出
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()