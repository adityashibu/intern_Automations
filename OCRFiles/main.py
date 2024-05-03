import pytesseract
from PIL import Image
import re

def extract_text_from_image(image_path):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def find_title(text):
    # Initialize variables to store information
    title = "Untitled Document"
    name = ""
    amount = ""

    # Check if "Dear" is mentioned in the text
    if "Dear" in text:
        # Extract the name following "Dear"
        name_match = re.search(r'Dear\s+([\w\s]+)', text)
        if name_match:
            name = name_match.group(1).strip()

    # Check if "AED" is mentioned in the text
    if "AED" in text:
        # Extract the amount following "AED"
        amount_match = re.search(r'AED\s+([\d.]+)', text)
        if amount_match:
            amount = amount_match.group(1).strip()

    # Construct the title
    if name and amount:
        title = f"{name} Bank receipt AED {amount}"
    elif name:
        title = f"{name} Bank receipt"

    return title

# Example usage:
image_path = r"D:\Screenshot 2024-05-03 123820.jpg"
text = extract_text_from_image(image_path)
title = find_title(text)
print("Title:", title)
print("Extracted Text:", text)
