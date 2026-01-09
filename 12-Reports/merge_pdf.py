from PyPDF2 import PdfMerger
from read_with_pdfplumber import read_pdf

merger = PdfMerger()
merger.append("sample.pdf")
merger.append("report.pdf")
merger.write("merger.pdf")
merger.close()

read_pdf("merger.pdf")
