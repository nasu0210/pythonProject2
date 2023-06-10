import pandas as pd

df=pd.read_excel('c:/data2/급식실시현황(초).xlsx', skiprows=1)
print(df.head().to_string())
filtered_df = df[df['급식종류'] == '직영']

# 추출된 열 출력
print(filtered_df)