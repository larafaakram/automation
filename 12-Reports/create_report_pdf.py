from reportlab.pdfgen import canvas

def create_report_lab():
    c = canvas.Canvas('report.pdf')
    c.drawString(100, 750, "Hello, This is a report PDF for testing")
    c.drawString(100, 700, "We are learning how read PDF with Python")
    c.save()

create_report_lab()