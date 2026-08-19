import numpy as np
import cv2
from scipy.stats import alpha

img= cv2.imread('obstacle.png')#图片
h,w,c= img.shape
print(f"高:{h},宽{w},通道{c}")#图片基本数据

crop_img=img[30:120,20:80]#图片剪裁y开始：y结束，x开始：x结束

alpha=1.3#对比度，大于1越大越强
beta=40#亮度越大越亮
bright_img=cv2.convertScaleAbs(img,alpha=alpha,beta=beta)

blur_img=cv2.GaussianBlur(bright_img,(9,9),0)#高斯模糊，模糊内核必须是奇数，越大越模糊

cv2.imshow("原图",img)
cv2.imshow("裁剪",crop_img)
cv2.imshow("增亮",bright_img)
cv2.imshow("高斯模糊",blur_img)

cv2.waitKey(0)#任意键
cv2.destroyAllWindows()#关闭窗口
