jd=[1,2,3,4,1,2,3,4,1,2]
hd=[1,1,2,4,1,2,3,1,2,2]
c=0
for i,j in zip(jd,hd):
    if i==j:
        c+=1
print(c)
