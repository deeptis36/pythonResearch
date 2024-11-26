import cv2
import pytesseract

# If you're on Windows, specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Use the correct path obtained from the which command

# Load the image using OpenCV
image_path = 'image_or_resume.jpg'  # Replace with your image file
image = cv2.imread(image_path)

# Optional: Convert the image to grayscale (improves OCR accuracy)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Optional: Apply image preprocessing (thresholding)
# This can help improve text extraction quality
_, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(thresh_image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)

# Optional: Display the image with OpenCV (useful for debugging)
cv2.imshow('Image', image)
cv2.imshow('Thresholded Image', thresh_image)
cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.destroyAllWindows()
