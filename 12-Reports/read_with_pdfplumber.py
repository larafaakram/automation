import pdfplumber

file = "sample.pdf"

def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            print(f"\n--- Page {i+1} ---\n{text}")

read_pdf(file)