import pandas as pd

df=pd.read_excel('c:/data3/test200.xlsx',
                 skiprows=4)
df=df[['능력단위명' ]]
li = list(range(660))
k = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 8, 8, 8, 8, 5, 8, 8, 8, 8, 5, 8, 8, 8, 6, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 6]
n=['4/24', '4/25', '4/26', '4/27', '4/28', '5/2', '5/3', '5/4', '5/8', '5/9', '5/10', '5/11', '5/12', '5/15', '5/16', '5/17', '5/18', '5/19', '5/22', '5/23', '5/24', '5/25', '5/26', '5/30', '5/31', '6/1', '6/2', '6/5', '6/7', '6/8', '6/9', '6/12', '6/13', '6/14', '6/15', '6/16', '6/19', '6/20', '6/21', '6/22', '6/23', '6/26', '6/27', '6/28', '6/29', '6/30', '7/3', '7/4', '7/5', '7/6', '7/7', '7/10', '7/11', '7/12', '7/13', '7/14', '7/17', '7/18', '7/19', '7/20', '7/21', '7/24', '7/25', '7/26', '7/27', '7/28', '7/31', '8/1', '8/2', '8/3', '8/4', '8/7', '8/8', '8/9', '8/10', '8/11', '8/14', '8/16', '8/17', '8/18', '8/21', '8/22', '8/23', '8/24', '8/25']
result = []

start_idx = 0
for length in k:
    result.append(li[start_idx:start_idx+length])
    start_idx += length

# for i,v in enumerate(result):
#     print(i,v)
print('-'*50)
#print(li1.index('5/24'))
#dday=input("출력할 일자(ex 5/24): ")
import datetime

di=datetime.date.today()
dday=str(di.month)+"/"+str(di.day)
day=n.index(dday)
#day =int(input("출력할 일자를 입력하세요: "))
#print(result[day-1])
#for i in result[21-1]:

print(df.loc[result[day]])
#print(df)

