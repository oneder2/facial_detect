#import matplotlib.pyplot as plt
# import imutils
import time
import signal
import cv2
# import os
import RPi.GPIO as GPIO
#import numpy as np

# 摄像头人脸识别

########## 配置参数 ###########
CAM_ID=0
THRESHOLD=100
GPIO_BEEPER=18
###############################

loop = 1

def beep_startup():
    for i in range(5):
        GPIO.output(GPIO_BEEPER, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(GPIO_BEEPER, GPIO.LOW)
        time.sleep(0.1)

def beep_alarm():
#   for i in range(5):
    GPIO.output(GPIO_BEEPER, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GPIO_BEEPER, GPIO.LOW)
    time.sleep(0.1)

def handler_exit(signalNumber, frame):
    loop = 0

print("Program begin")

signal.signal(signal.SIGQUIT, handler_exit)
signal.signal(signal.SIGTERM, handler_exit)

# 使用haarcascades的正脸模型
face_detector = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml')

# 打开摄像
cap = cv2.VideoCapture(CAM_ID) # cap代表被打开的摄像头

# 初始化蜂鸣器的GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_BEEPER, GPIO.OUT)

# 启动提示
beep_startup()

while loop:
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
            beep_alarm()

cap.release()
GPIO.cleanup()

print("Program end")

