# Braille ETL Pipeline – Flickdone Assessment

## 🧠 Project Overview

This project demonstrates a simplified version of Flickdone's internal data preparation pipeline to convert unstructured textual content (from scanned pages) into structured, AI-trainable datasets for Braille translation. The output is a **plain-text to Braille parallel corpus**, using open-source tools like **Tesseract OCR** and **Liblouis**.

---

## 🔧 Tools & Libraries Used

| Tool          | Purpose                                      |
|---------------|----------------------------------------------|
| Python        | Scripting language                           |
| Tesseract OCR | Extract text from scanned `.jpeg` images     |
| Liblouis      | Convert English text into Braille            |
| JSON          | Store structured data (text and braille)     |
| subprocess    | Interface with external command-line tools   |

---

## 📁 File Structure

```
braille-etl-pipeline/
├── all_files_json_file.py      # OCR script
├── json_to_braille.py          # Braille translation script
├── ocr_output.json             # Cleaned OCR results
├── braille_output.json         # Final Braille parallel corpus
├── README.md                   # This file
```

---

## ⚙️ How the Pipeline Works

### ✅ Step 1: Extract Text using Tesseract OCR
- The script `all_files_json_file.py` scans a folder of `.jpeg` files.
- Extracted text is cleaned and saved into `ocr_output.json`.

### ✅ Step 2: Convert Text to Braille
- The script `json_to_braille.py` reads `ocr_output.json`.
- It uses `Liblouis` (via `subprocess`) to convert text into Braille.
- The output is saved as `braille_output.json`, a parallel corpus.

---

## ▶️ How to Run

### 1. 🔹 Install Requirements

```bash
pip install pytesseract pillow
```

Also install Tesseract OCR (Windows):

- Download and install from: https://github.com/tesseract-ocr/tesseract

Install Liblouis:

- Download from: https://github.com/liblouis/liblouis/releases
- Extract `lou_translate.exe` and place it in `C:\liblouis\bin\`

---

### 2. 🔹 Run the OCR Script

- Edit the image folder path inside `all_files_json_file.py`, then run:

```bash
python all_files_json_file.py
```

➡️ Output: `ocr_output.json`

---

### 3. 🔹 Run Braille Conversion

- Update the `liblouis_exe` path in `json_to_braille.py` to match your machine:

```python
liblouis_exe = r'C:\liblouis\bin\lou_translate.exe'
```

Then run:

```bash
python json_to_braille.py
```

➡️ Output: `braille_output.json`

---

## 📊 Example Output Format (`braille_output.json`)

```json
{
  "gita1.jpeg": {
    "original_text": "The Bhagavad Gita...",
    "braille_text": ",! ,bhagavad ,gita..."
  }
}
```

## 🙏 Acknowledgments

Thanks to Flickdone for this unique opportunity to build for accessibility and inclusion through AI.
