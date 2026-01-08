from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=13)
pdf.multi_cell(190, 10, txt="Hello! This is a sample text for testing! Enjoy Automation!")
pdf.add_page() # Add second page
pdf.multi_cell(190, 10, txt="Hello! This is a sample text for testing! Enjoy Automation!")
pdf.output("pdf_sample.pdf")