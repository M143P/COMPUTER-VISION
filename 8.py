import cv2

image = cv2.imread("C:\GOPI\IMG-20240105-WA0015.jpg")
rotated_image = cv2.transpose(image)
rotated_image = cv2.flip(rotated_image, 0) 
cv2.imshow('Original Image', image)
cv2.imshow('270-Degree Clockwise Rotated Image', rotated_image)

cv2.waitKey(0) 
cv2.destroyAllWindows()
