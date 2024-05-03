import pytesseract
import PyPDF2
from PIL import Image
import io

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            # Convert each page to an image
            img = page_to_image(page)
            # Extract text from the image using Tesseract
            page_text = pytesseract.image_to_string(img)
            text += page_text + "\n\n"
    return text

def page_to_image(page):
    # Convert PDF page to an image
    img = page.to_pil()
    # Convert to RGB if image is not in RGB format
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img

def find_title(text):
    # Implement your logic to find the title based on the extracted text
    # For example, you might look for the first line that contains capitalized words
    lines = text.split('\n')
    for line in lines:
        if line.strip().isupper():  # Assuming titles are in all caps
            return line.strip()
    # If no suitable title found, return a default title
    return "Untitled Document"

# Example usage:
pdf_path = '/path/to/your/pdf/document.pdf'
text = extract_text_from_pdf(pdf_path)
title = find_title(text)
print("Title:", title)
print("Extracted Text:", text)
