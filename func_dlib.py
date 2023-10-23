import cv2          # Opencv를 사용하여 영상처리 및 카메라 설정에 사용
import dlib         # 얼굴인식 및 랜드마크 예측을 위한 라이브러리
from functools import wraps     # 함수 데코레이터를 활용하기 위한 라이브러리
from scipy.spatial import distance #유클리드 거리 계산에 사용
import time             # 시간 관련 기능을 사용하기 위한 라이브러리
import os               # 운영체제 관련 기능을 사용하기 위한 라이브러리
import threading

def calculate_EAR(eye): # 눈 거리 계산 test1
   A = distance.euclidean(eye[1], eye[5])
   B = distance.euclidean(eye[2], eye[4])
   C = distance.euclidean(eye[0], eye[3])
   ear_aspect_ratio = (A+B)/(2.0*C)
   return ear_aspect_ratio

#GPIO Warning dismiss

# 카메라 셋팅
cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
cap.set(3, 320)
cap.set(4, 480)

# dlib 인식 모델 정의
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("C:\\python\\opencv\\opencv\\ch01\\shape_predictor_68_face_landmarks.dat")



def dlib_func(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = hog_face_detector(gray)
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        leftEye = []
        rightEye = []

        for n in range(36,42): # 오른쪽 눈 감지
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x,y))
            next_point = n+1
            if n == 41:
               next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            #cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        for n in range(42,48): # 왼쪽 눈 감지
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x,y))
            next_point = n+1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            #cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)

        EAR = (left_ear+right_ear)/2
        EAR = round(EAR,2)

        if EAR<0.18:
            return True
                     
        print(EAR)

def cascade_func(frame):
    xml = "C:\\python\\opencv\\opencv\\ch01\\data\\haarcascades\\haarcascade_eye_tree_eyeglasses.xml"
    face_cascade = cv2.CascadeClassifier(xml)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2_faces = face_cascade.detectMultiScale(gray, 1.05, 5)

    if len(cv2_faces) == 0:
        return True
    else:
        return False


closed_flag = False
front_flag = False

while True:
    _, frame = cap.read()
    

    if dlib_func(frame) == True:
        closed_flag = True
        cv2.putText(frame,"Closed",(20,100), cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
    
        
    if cascade_func(frame) == True:
        front_flag = True
        cv2.putText(frame,"Front",(20,100), cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
    
    cv2.imshow("Are you Sleepy?", frame)

    key = cv2.waitKey(30)
    if key == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
