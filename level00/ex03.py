import PyPDF2

file = open('c:/data3/abcde.pdf', 'rb')
reader = PyPDF2.PdfReader(file)


    # 페이지 수 확인
num_pages = len(reader.pages)
print("Number of pages:", num_pages)

    # 페이지 별로 텍스트 추출
for page_number in range(num_pages):
    page = reader.pages[page_number]
    text = page.extract_text()
    print("Page", page_number + 1, ":", text)
