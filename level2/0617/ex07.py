k=[6,1,2,3,2,4,5,10]
s=1
c=0
while s<6:
    if s!=k[c]:

        k.remove(k[c])
        c+=1
    print(s)
    s+=1
print(k)
