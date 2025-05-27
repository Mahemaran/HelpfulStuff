import easyocr
import cv2

def read_text_from_image(image_path):
    # Initialize EasyOCR reader with English language
    reader = easyocr.Reader(['en'])
    # Read the image
    image = cv2.imread(image_path)
    # Perform OCR
    results = reader.readtext(image_path)
    print("Detected Text:")
    for (bbox, text, prob) in results:
        print(f"{text}")
read_text_from_image(r"C:\Users\DELL\Downloads\1.png")