import PyPDF2

def read_pdf(file):
    with open(file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"Page {i+1}:")
            print(text)