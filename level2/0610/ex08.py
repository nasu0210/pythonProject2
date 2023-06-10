day=['5/4','5/12','5/16','6/3','6/5','6/9']
fruit=['사과','포도','사과','포도','사과','포도']
count=[5,4,7,2,5,4]
li=[]
for d,f,c in zip(day,fruit,count):
    if f=='사과':
        li.append(c)
for d, f, c in zip(day, fruit, count):
    if c==max(li):
        print(d)

