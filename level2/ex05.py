import pandas as pd
df = pd.read_excel('c:/data3/test200.xlsx',skiprows=4)
print(df)
# 특정 칼럼부터 데이터 선택
start_column = 4  # 시작 칼럼
end_column = 9    # 끝 칼럼
df= df.iloc[:, [0,3,4,5,6,7,8]]

# 선택한 칼럼과 해당 데이터 출력
df=df.set_index('일차')

print(df.iloc[df.index.get_loc('3일차'):df.index.get_loc('4일차')])