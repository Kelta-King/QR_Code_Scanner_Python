# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('road.jpg')

# Extracting the height and width of an image
# h, w = image.shape[:2]
# # Displaying the height and width
# print("Height = {}, Width = {}".format(h, w))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('image.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

