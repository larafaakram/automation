from reportlab.pdfgen import canvas

c = canvas.Canvas("generated_report.pdf")
c.drawString(100, 750, "This a generated PDF Report")
c.save()