# PageScan

PageScan is a small OCR batch pipeline for comic pages and webtoon strips. It reads a single image, detects text regions, saves a preview image with boxes, and exports structured JSON results.

This repository is set up as a starter project for the first milestones in the plan:

- Step 1: read a page and print text
- Step 2: detect text regions and draw boxes
- Step 3: export a stable JSON format

## Project structure

- `scan.py` – command-line entry point
- `pagescan/` – package modules for loading images, OCR, drawing, and export
- `tests/` – pytest tests for the core helpers
- `requirements.txt` – Python dependencies

## Quick start

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # or .venv\Scripts\activate  # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add a test image under `samples/` and run:

   ```bash
   python scan.py samples/page1.png --min-confidence 0.3
   ```

4. The script will:

   - read the page with Pillow
   - run OCR with EasyOCR
   - print each detected line of text
   - save a preview with boxes to `output/page1_boxes.png`
   - save structured data to `output/page1.json`

## Notes

- EasyOCR downloads model data on first use, so the first run can be slow.
- This project intentionally keeps the early implementation simple and testable before adding archive and webtoon support.
- The code is written to avoid common pitfalls like NumPy scalar serialization errors when saving JSON.
