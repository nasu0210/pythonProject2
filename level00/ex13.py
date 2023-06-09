import pandas as pd

df=pd.read_excel('c:/data3/test200.xlsx',
                 skiprows=4)
df=df[['능력단위명' ]]
m = [i for i in range(1, 664//8+1) for _ in range(8)]
m=m[:-4]
df['일차'] = m
df=df[['일차','능력단위명' ]]
print(df.to_string())
input_day = input("출력할 일차를 입력하세요: ")




filtered_df = df[df['일차'] == int(input_day)]
print(filtered_df.to_string(index=False))