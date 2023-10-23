# #하나하나 이미지를 출력

# import matplotlib.pyplot as plt
# import cv2

# imgBGR = cv2.imread('cat.bmp')
# imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# plt.axis('off')
# plt.imshow(imgRGB)
# plt.show()


# # 그레이스케일 영상 출력
# imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

# plt.axis('off')
# plt.imshow(imgGray, cmap = 'gray')
# plt.show()


# 한번에 두개의 이미지 출력
import matplotlib.pyplot as plt
import cv2

#컬러 영상 & 그레이스케일 영상 불러오기
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_RGB2BGR)
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

img_sample1 = cv2.imread('img_opencv_sample.jpg')
RGB_img_sample1 = cv2.cvtColor(img_sample1, cv2.COLOR_RGB2BGR)

img_sample2 = cv2.imread('img_opencv_sample2.jpg')
RGB_img_sample2 = cv2.cvtColor(img_sample2, cv2.COLOR_RGB2BGR)

#두 개의 영상을 함께 출력
plt.subplot(141), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(142), plt.axis('off'), plt.imshow(imgGray, cmap = 'gray')
plt.subplot(143), plt.axis('off'), plt.imshow(RGB_img_sample1)
plt.subplot(144), plt.axis('off'), plt.imshow(RGB_img_sample2)
plt.show()