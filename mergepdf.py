from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files= os.listdir()

for pdf in files:
    if pdf.endswith(".pdf"):
        merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()