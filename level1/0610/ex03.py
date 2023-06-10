jd=[1,2,3,4,1,2,3,4,1,2]
hd=[1,1,2,4,1,2,3,1,2,2]
count=0
for i,v in enumerate(jd):
    if v==hd[i]:
        count+=1
print(count)

