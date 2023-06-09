c=0
for i in range(10):
    for j in range(i, 10):
        #print(i,j)
        print('-------------')
        for k in range(j, 10):#9
            print(j, k)
            #print((i, j, k))
            c=c+1

print(c)
