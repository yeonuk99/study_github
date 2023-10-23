import sys
import cv2

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp') #cat.bmp파일을 불러와 img변수에 저장
img2 = cv2.imread('img_opencv_sample.jpg')
img3 = cv2.imread('img_opencv_sample2.jpg')
img4 = cv2.imread('img_opencv_sample3.jpg')

if img is None: #영상 파일 불러오기가 실패하면 에러 메시지를 출력하고 종료
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image1')    # "image"라는 이름의 새 창을 만들고
cv2.namedWindow('image2')
cv2.namedWindow('image3')
cv2.imshow('image1', img)    # 이 창에 img 영상을 출력하고
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.imshow('image', img4)
cv2.waitKey()               # 키보드 입력이 있을 떄까지 대기

cv2.destroyAllWindows()     # 생성된 모든 창을 닫음
