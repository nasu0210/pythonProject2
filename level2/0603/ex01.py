li=[]

for i in range(0,101):
    #print((i%10*10)+i//10)
    if ((i%10*10)+i//10) not in li:
       li.append(i)


for j in li:
    print(j)
