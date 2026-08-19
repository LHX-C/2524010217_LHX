# Software_C1 OpenCV基础图像处理
## 一、学习过程
1. 环境准备阶段
先熟悉项目需要用到的工具库，完成 Python、OpenCV‑python、numpy 库安装；查找人脸检测 Haar‑cascade 模型文件，区分相对路径、绝对路径，准备好人脸测试图片，熟悉编辑器运行环境。
基础图像处理分步实操学习
2. 依次拆开每一项基础功能进行练习：首先掌握图像加载、预览、保存；接着理解图片数组结构，练习图像切片裁剪；再学习像素计算公式，调试亮度、对比度增强效果；最后熟悉高斯模糊卷积核参数，观察不同核大小带来的模糊差异，逐个打通基础图像接口。
3. 人脸检测模块学习
了解 Haar 级联检测器的调用方式，加载人脸模型文件；研读人脸检测函数入参含义，看懂检测返回的 x、y、宽、高坐标；练习根据坐标截取人脸感兴趣区域，对人脸单独模糊后覆盖回原图，完成静态图片人脸打码。
4. 实时视频人脸模糊学习
学习摄像头调用接口，掌握循环读取每一帧画面；在循环内重复执行人脸检测、人脸区域模糊逻辑；添加键盘退出监听。
5. 功能整合与梳理
将图像加载、裁剪、亮度对比度调节、高斯模糊、人脸检测、人脸模糊整套流程串联；整理每一个接口作用、容易出错的细节，搭建完整的处理逻辑。
-------------------------------------------------------------------------------------
## 二、关键知识点
1. 图像底层基础
OpenCV 读取图像通道顺序为 BGR，和常规 RGB 图片通道顺序不一样。
图像本质是 NumPy 三维数组，排布顺序为 [图像高度，图像宽度，通道]，裁剪、修改像素都是数组运算。
单个像素取值范围固定为 0‑255，像素运算之后需要限制区间，防止数值溢出。
2. 基础图像处理
图像加载：cv2.imread()，路径含有中文容易读取失败。
图像裁剪：依靠数组切片 img[y起始:y结束, x起始:x结束]，y 代表纵向、x 代表横向。
对比度、亮度调整：计算公式 dst = α * src + β；α 控制对比度，β 控制画面明暗。
高斯模糊：cv2.GaussianBlur；模糊卷积核必须为奇数，核尺寸越大模糊效果越强。
3. Haar‑Cascade 人脸检测
依靠预训练好的 xml 级联模型，滑动窗口检测图片内正面人脸。
检测结果参数：x、y 为人脸左上角坐标，w、h 分别代表人脸宽度、高度。
ROI 感兴趣区域：利用人脸坐标截取人脸局部画面，单独做模糊处理再回填原图。
4. 摄像头实时流处理
摄像头工作原理为循环不断读取单帧图像，每一帧等同于一张独立图片。
waitKey() 实现键盘按键监听，用来控制程序退出。
程序结束必须释放摄像头资源、销毁所有图像窗口，避免硬件被程序占用。
-------------------------------------------------------------------------------------
## 三、踩坑记录
1. 彩色图与灰度通道不匹配
原因：人脸区域裁剪后转为灰度图（单通道 H,W），再赋值给彩色原图（三通道 H,W,3），通道数目不一致
解决：直接对彩色原图人脸高斯模糊
2. 高斯模糊内核尺寸必须为奇数
原因：内核尺寸写的是偶数
解决：内核尺寸改为奇数
-------------------------------------------------------------------------------------
## 四、OpenCV‑Python 常用函数详细用法
1. 图像读写与窗口操作函数
cv2.imread
作用：从磁盘加载图像
参数说明：路径尽量不用中文；默认彩色读取；0 代表灰度图读取
返回值：numpy 数组
cv2.imshow
新建窗口展示图像
cv2.imwrite
将处理完成的图片保存至本地
cv2.waitKey
等待键盘输入；0 代表无限等待；视频流一般设置 1‑30
cv2.destroyAllWindows()
销毁全部图像窗口，释放 GUI 资源
2. 图像裁剪
裁剪依靠 numpy 数组切片
plaintext
img[y1:y2, x1:x2]
y：竖直方向（行），x：水平方向（列）
y2 = 起始 y + 区域高度；x2 = 起始 x + 区域宽度
3. 亮度、对比度调节
cv2.convertScaleAbs(src, alpha=对比度系数, beta=亮度偏移)
alpha＞1：对比度升高；0<alpha<1：对比度降低
beta 正数提亮画面，负数降低亮度
函数自带像素截断，自动约束 0~255，防止溢出
4. 高斯模糊
cv2.GaussianBlur(src, ksize=(宽,高), sigmaX)
ksize 卷积核尺寸，只能填写奇数如 (3,3)、(5,5)
内核数值越大，模糊强度越高
sigmaX：X 方向高斯核标准差；数值越大画面越模糊
5. 摄像头视频读取
cap = cv2.VideoCapture(设备编号)，电脑内置摄像头一般传入 0
ret, frame = cap.read() 读取一帧画面；ret 为读取成功标记，frame 为图像
cap.release() 关闭摄像头，释放硬件占用
6. Haar 级联人脸检测器相关函数
cv2.CascadeClassifier("xml模型路径")
加载预训练人脸检测模型文件
detectMultiScale(image, scaleFactor, minNeighbors, minSize)
scaleFactor：窗口缩放比例，一般取 1.1
minNeighbors：候选检测框最低筛选数量，数值越高误检越少
minSize：可识别人脸最小像素尺寸，过滤过小的干扰区域
返回结果：数组列表，每一组 [x,y,w,h]
-------------------------------------------------------------------------------------
## 五、摄像头实时人脸模糊流程
初始化摄像头 VideoCapture
加载人脸检测模型
while 循环持续读取每一帧画面
当前帧执行人脸检测
人脸区域切片、高斯模糊、回填画面
展示处理之后的实时画面
监听键盘按键，按下退出键跳出循环
释放摄像头、销毁全部窗口
-------------------------------------------------------------------------------------
## 六、代码
'''python
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
'''
-------------------------------------------------------------------------------------
'''python
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
'''
-------------------------------------------------------------------------------------
'''python
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
'''
