import cv2
import numpy as np

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')#opencv自带人脸模型

img = cv2.imread("Kobe.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转为灰度图，人脸检测必须使用灰度图像
faces = face_detector.detectMultiScale(gray, 1.3, 5)#检测人脸，返回人脸框xywh
for (x,y,w,h) in faces:#循环遍历所有人脸
    face_area = img[y:y+h,x:x+w]#用原图截取人脸区域，因为是BRG三通道，而非灰度图二通道
    blur_face = cv2.GaussianBlur(face_area,(25,25),0)#高斯模糊
    img[y:y+h,x:x+w] = blur_face#模糊后的人脸放回原图

cv2.imshow("img",img)#输出
cv2.waitKey(0)
cv2.destroyAllWindows()