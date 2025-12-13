import cv2

# Read image
img = cv2.imread("D:\Python Cidrie\JJe.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection using Canny
edges = cv2.Canny(gray, 100, 200)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
