c=0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if (i+j+k)==10:
                print(i, j, k)
                c+=1
print(c)