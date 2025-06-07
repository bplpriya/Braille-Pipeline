# 🧠 Braille ETL Pipeline – Flickdone Assessment

This project simulates a core part of Flickdone’s AI data preparation workflow: **converting unstructured scanned documents into a structured parallel corpus for Braille translation**.  
It supports **multi-language OCR (e.g., English and Korean)** and uses **Liblouis** to generate Braille equivalents.

---

## 🌐 Languages Supported

- ✅ English (Grade 2 Braille)
- ✅ Korean (Grade 1 Braille via custom table)

---

## 🔧 Tools & Libraries Used

| Tool          | Purpose                                      |
|---------------|----------------------------------------------|
| Python        | Core scripting language                      |
| Tesseract OCR | Text extraction from image files             |
| Liblouis      | Conversion of text to Braille (via CLI)      |
| Pillow        | Image file handling                          |
| JSON          | Structured output format                     |
| subprocess    | Interface with external command-line tools   |

---

## 📁 Project Structure

```
braille-etl-pipeline/
├── all_files_json_file.py       # OCR script for English
├── all_files_json_korean.py     # OCR script for Korean
├── json_to_braille.py           # English Braille converter
├── json_to_braille_korean.py    # Korean Braille converter
├── ocr_output.json              # English OCR output
├── ocr_output_korean.json       # Korean OCR output
├── braille_output.json          # English Braille output
├── braille_output_korean.json   # Korean Braille output
├── ko-g1.ctb                    # Korean Braille table (downloaded)
├── README.md                    # Project overview (this file)
```

---

## ⚙️ How the Pipeline Works

### ✅ Step 1: OCR Extraction

- `all_files_json_file.py` → Scans `.jpeg` images in a folder and extracts **English text** using `pytesseract`.
- `all_files_json_korean.py` → Same as above, but uses language code `'kor'` to extract **Korean text**.
- Outputs: `ocr_output.json`, `ocr_output_korean.json`

### ✅ Step 2: Braille Conversion

- `json_to_braille.py` → Converts extracted English text to **Grade 2 English Braille** using Liblouis (`en-us-g2.ctb`).
- `json_to_braille_korean.py` → Converts extracted Korean text to **Grade 1 Korean Braille** using a custom downloaded table (`ko-g1.ctb`).
- Outputs: `braille_output.json`, `braille_output_korean.json`

---

## ▶️ How to Run the Project

### 1. 🔹 Install Required Libraries

```bash
pip install pytesseract pillow
```

Also install:

- Tesseract OCR → [Install Tesseract](https://github.com/tesseract-ocr/tesseract)
- Liblouis → [Download Liblouis](https://github.com/liblouis/liblouis/releases)

> Place `lou_translate.exe` in a known path like:
> `C:\liblouis\bin\lou_translate.exe`

---

### 2. 🔹 Run English OCR & Braille

```bash
python all_files_json_file.py         # Creates ocr_output.json
python json_to_braille.py             # Creates braille_output.json
```

---

### 3. 🔹 Run Korean OCR & Braille

```bash
python all_files_json_korean.py       # Creates ocr_output_korean.json
python json_to_braille_korean.py      # Creates braille_output_korean.json
```

Make sure you download `ko-g1.ctb` from:  
📁 https://github.com/liblouis/liblouis/blob/master/tables/ko-g1.ctb

Place it in:  
`C:\liblouis\share\liblouis\tables\ko-g1.ctb`

Update this path inside your Korean Braille script.

---

## 📊 Sample Output Format

### `braille_output.json` (English)

```json
{
  "gita1.jpeg": {
    "original_text": "The Bhagavad Gita is a sacred text...",
    "braille_text": ",! bhagavad ,gita is a sacred text..."
  }
}
```

### `braille_output_korean.json` (Korean)

```json
{
  "k4.jpeg": {
    "original_text": "시를 통해 보다 빠르고 쉽게 측정 그래프를...",
    "braille_text": "⠱⠊⠙⠑⠗ ⠞⠓⠕⠥⠛⠓ ⠃⠕⠗..."
  }
}
```

---

## 🧪 Testing & Validation

- OCR outputs were visually validated for correctness (for both English and Korean).
- Braille outputs were cross-checked with sample outputs generated from trusted online converters and documentation.

---

## ❓ Possible Interview Questions

| Question | Suggested Answer |
|---------|------------------|
| **Why use JSON?** | It’s lightweight, human-readable, and ideal for structured parallel corpus generation. |
| **Why use Liblouis?** | It’s the industry-standard open-source Braille translator supporting over 70 languages. |
| **What challenge did you face with Korean?** | Korean OCR needed explicit `lang='kor'` and a custom `ko-g1.ctb` Braille table not bundled by default. |
| **How does the ETL work?** | The pipeline extracts (OCR), transforms (via Liblouis), and loads (into JSON) for structured AI training. |
| **What is the difference between Grade 1 and Grade 2 Braille?** | Grade 1 represents each letter directly. Grade 2 includes contractions for efficiency and is more commonly used. |

---

## 🙏 Acknowledgments

Thanks to **Flickdone** for this meaningful project that contributes toward accessibility, inclusion, and assistive AI technologies.

---