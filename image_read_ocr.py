import cv2
import pytesseract
from PIL import Image

# Point to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Load the image using OpenCV
image = cv2.imread('images/handwritten_image.png')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
binary_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Optionally denoise the image
binary_image = cv2.medianBlur(binary_image, 3)

# Save preprocessed image (optional)
cv2.imwrite('preprocessed_image.png', binary_image)

# Use Tesseract with custom configurations
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(binary_image, config=custom_config)

print(text)
