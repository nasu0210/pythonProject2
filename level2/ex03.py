import pandas as pd
df = pd.read_excel('c:/data3/days00.xlsx')
df['time']=8
print(df)
value_to_change = [['06-09',5], ['06-16',5],['06-23',5],['06-29',6],
                   ['06-30',1],['08-25',6]]
data_list = df.values.tolist()
for v in value_to_change:
    for d in data_list:
        if v[0]==d[0]:
            d[2]=v[1]

print(data_list)
df = pd.DataFrame(data_list, columns=['Date', 'Day', 'Value'])

# Excel 파일에 저장
df.to_excel('c:/data3/days000.xlsx', index=False)