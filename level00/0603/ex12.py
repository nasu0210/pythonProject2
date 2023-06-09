c=0
for i in range(1,1001):
    if sum(map(int,list(str(i))))==10:
        print(i)
        c+=1
print(c)