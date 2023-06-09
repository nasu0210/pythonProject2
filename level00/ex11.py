from openpyxl import load_workbook

# 엑셀 파일 로드
workbook = load_workbook('c:/data3/test200.xlsx')

# 원하는 시트 선택
sheet = workbook['시간표_이만복강사']

# 읽고자 하는 셀 범위 설정
start_row = 6
end_row = 6
start_column = 'A'
end_column = 'L'
cell_range = f'{start_column}{start_row}:{end_column}{end_row}'

# 셀 범위의 서식 읽기
for row in sheet[cell_range]:
    for cell in row:
        cell_format = cell.number_format
        print(f'셀 {cell.coordinate}의 서식: {cell_format}')

# 엑셀 파일 닫기
workbook.close()
