import json
import subprocess
from pathlib import Path

# Paths
input_json_path = 'ocr_output_korean.json'
output_json_path = 'braille_output_korean.json'

# Path to lou_translate.exe and translation table (change this if needed)
liblouis_exe = r'C:\liblouis-3.33.0-win64\bin\lou_translate.exe'
braille_table = 'ko-g1.ctb'

# Load OCR text from JSON
with open(input_json_path, 'r', encoding='utf-8') as f:
    ocr_data = json.load(f)

braille_data = {}

# Translate each text block to Braille
for filename, content in ocr_data.items():
    text = content.get("text", "")
    
    # Call Liblouis
    result = subprocess.run(
        [liblouis_exe, braille_table],
        input=text.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    braille_output = result.stdout.decode('utf-8')
    braille_data[filename] = {
        "original_text": text.strip(),
        "braille_text": braille_output.strip()
    }

# Save translated Braille text to a new JSON file
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(braille_data, f, indent=4, ensure_ascii=False)

print(f"✅ Korean Braille translation saved to {output_json_path}")
