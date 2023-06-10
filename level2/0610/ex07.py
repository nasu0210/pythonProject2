day=['5/4','5/12','5/16','6/3','6/5','6/9']
fruit=['사과','포도','사과','포도','사과','포도']
count=[5,4,7,2,5,4]
p1,p2,p3,p4=0,0,0,0
for d,f,c in zip(day,fruit,count):
    m=int(d.split('/')[0])#5/4 ['5','4']
    if f=='사과':
        p1+=c
        if m==5:
            p4+=c
    if f=='포도':
        p2+=c
        if m==6:
            p3+=c
print(p1);print(p2);print(p3);print(p4)