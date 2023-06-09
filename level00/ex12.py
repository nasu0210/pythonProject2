from openpyxl import load_workbook

# 엑셀 파일 로드
workbook = load_workbook('c:/data3/test200.xlsx')

# 원하는 시트 선택
sheet = workbook['시간표_이만복강사']
k=(21)-1
# 읽고자 하는 셀 범위 설정
start_row = 6+k*8
end_row = 13+k*8
start_column = 'H'
end_column = 'H'
cell_range = f'{start_column}{start_row}:{end_column}{end_row}'
values = []
for row in sheet[cell_range]:
    row_values = []
    for cell in row:
        row_values.append(cell.value)
    values.append(row_values)

# 가져온 값 출력
for i,row in enumerate(values):
    print(i+1,row[0])

# 엑셀 파일 닫기
workbook.close()