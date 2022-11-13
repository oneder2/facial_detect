#import matplotlib.pyplot as plt
# import imutils
import time
import cv2
# import os
import RPi.GPIO as GPIO
import numpy as np

# 摄像头人脸识别
CAM_ID=0
THRESHOLD=100

# 使用opencv提供的人脸识别算法(人脸识别器)
face_detector = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml')

# 打开摄像
cap = cv2.VideoCapture(CAM_ID) # cap代表被打开的摄像头

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.1)

while 1:
    time.sleep(0.1)
    # 从摄像头中读取一帧数据
    ret, frame = cap.read() # frame 存储了读取到的数据
    
    # 将获取到的数据进行灰度处理
    #gray = cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
#     cv2.imshow('img',gray)
    # 在进行灰度处理后的图片中识别人脸
    faces = face_detector.detectMultiScale(frame) # 被识别到的多张人脸
    for x,y,w,h in faces:
        print(w) #人脸d
        if w > THRESHOLD:
            print("///Warning///")
#            for i in range(5):
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
        

    # cv2.imwrite('tong.jpg',frame)
cap.release()
GPIO.cleanup()


"""
# 摄像头人脸识别

# 使用opencv提供的人脸识别算法(人脸识别器)
face_detector = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml')

# 打开摄像头
cap = cv2.VideoCapture(0) # cap代表被打开的摄像头

while 1:
    # 从摄像头中读取一帧数据
    ret, frame = cap.read() # frame 存储了读取到的数据
    
    # 将获取到的数据进行灰度处理
    gray = cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
#     cv2.imshow('img',gray)
    # 在进行灰度处理后的图片中识别人脸
    faces = face_detector.detectMultiScale(gray) # 被识别到的多张人脸
    for x,y,w,h in faces:
        cv2.circle(frame,(x+w//2,y+h//2),w//2,[0,255,0],2) # 用圆圈圈出识别人脸
    cv2.imshow('frame',frame)
    
    
    key = cv2.waitKey(1000//24)
    if key == ord('q'):
        break
    # cv2.imwrite('tong.jpg',frame)
cap.release()
cv2.destroyAllWindows()

"""
