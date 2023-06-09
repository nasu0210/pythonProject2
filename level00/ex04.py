#pip install PyMuPDF

import fitz

file = "c:/data3/aaa.pdf"
pdf = fitz.open(file)

for page_number in range(len(pdf)):
    page = pdf[page_number]
    text = page.get_text()
    print("Page", page_number + 1, ":", text)
