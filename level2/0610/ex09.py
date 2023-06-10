day=['5/4','5/12','5/16','6/3','6/5','6/9']
fruit=['사과','포도','사과','포도','사과','포도']
count=[5,4,7,2,5,4]
li1=[]
li2=[]
for d,f,c in zip(day,fruit,count):
    m = int(d.split('/')[0])  # 5/4 ['5','4']
    if m==5:
        li1.append(c)
    if m==6:
        li2.append(c)
print(sum(li1)/len(li1))
print(sum(li2)/len(li2))

