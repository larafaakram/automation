from reportlab.pdfgen import canvas


def create_sample_pdf():
    c = canvas.Canvas('sample.pdf')
    c.drawString(100, 750, "Hello, This is a sample PDF for testing!")
    c.drawString(100, 700, "we are learning how read PDF with Python.")
    c.save()

create_sample_pdf()