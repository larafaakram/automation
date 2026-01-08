from fpdf import FPDF

def create_pdf(text, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=13)
    pdf.multi_cell(190, 10, txt=text)
    pdf.output(output_file)
    print(f"PDF created at {output_file}")