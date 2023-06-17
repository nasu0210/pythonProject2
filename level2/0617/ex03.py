a=[100, 100, 63, 99, 89]
li=[]
for i in a:
    if a.count(i)>1:
        print(0)
    else:
        print(i)