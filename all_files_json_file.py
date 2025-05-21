from pathlib import Path
from PIL import Image
import pytesseract
import json

# Replace with your image folder path
directory = 'C:/Users/flickdone_intern'

# Path to save the JSON output
output_file = 'ocr_output.json'

# Dictionary to hold the results
ocr_results = {}

# Loop through all .jpeg files in the directory
files = Path(directory).glob('*.jpeg')
for file in files:
    text = pytesseract.image_to_string(Image.open(file))
    ocr_results[file.name] = {
        "text": text
    }

# Write results to a JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(ocr_results, f, indent=4, ensure_ascii=False)

print(f"OCR results saved to {output_file}")
