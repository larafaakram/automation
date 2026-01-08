from excel.read_excel import read_excel
from excel.write_excel import write_excel

from pdf.create_pdf import create_pdf
from pdf.read_pdf import read_pdf

data = read_excel("excel_demo.xlsx")
write_excel([{'Name': 'john', 'Age': 43}, {'Name': 'Jane', 'Age': 45}], 'output_excel.xlsx')

read_pdf("pdf_sample.pdf")
create_pdf("This is an automated PDF file created using Python!", "generated_pdf.pdf")

