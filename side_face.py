import cv2
import time
def main():
    camera = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    camera.set(3, 640)
    camera.set(4, 480)
    xml = "C:\\python\\opencv\\opencv\\ch01\\data\\haarcascades\\haarcascade_eye_tree_eyeglasses.xml"
    face_cascade = cv2.CascadeClassifier(xml)
    while camera.isOpened():
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        print("faces detected Number: " + str(len(faces)))
        
        for x, y, w, h in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("result", image)
    time.sleep(0.2)

    
cv2.destroyAllWindows()

if __name__ == "__main__":
    main()