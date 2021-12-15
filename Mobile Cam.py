import cv2
url = "http://ip address and port/video"
cp = cv2.VideoCapture(url)
while True:
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("CAM", frame)
    q = cv2.waitKey(1)
    if q ==ord("q"):
        break
cv2.destroyAllWindows()
