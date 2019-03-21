import cv2

image = cv2.imread('start_KF6.jpg', cv2.IMREAD_GRAYSCALE)

ret, image = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold image", image)
cv2.waitKey(-1)
cv2.destroyAllWindows()

