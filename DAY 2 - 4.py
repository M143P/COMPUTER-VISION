import cv2

def canny_edge_detection(image_path, low_threshold, high_threshold):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Error: Could not load image!")
        return
    blurred_img = cv2.GaussianBlur(img, (5, 5), 1.5)
    edges = cv2.Canny(blurred_img, low_threshold, high_threshold)
    cv2.imshow('Original Image', img)
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
canny_edge_detection("C:\GOPI\IMG-20240711-WA0013.jpg", 50, 150)
