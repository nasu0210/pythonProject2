li=[6,1,2,3,2,4,5,10]
c=0
for i in range(len(li)):
    if len(li)<=i:
        break
    if (i+1)!=li[c]:
        del li[c]
    c+=1
print(li)

