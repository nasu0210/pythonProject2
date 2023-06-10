jd=[1,2,3,4,1,2,3,4,1,2]
hd=[1,1,2,4,1,2,3,1,2,2]
 #  o x x o o o o x x o
count=0
for i in range(len(jd)):
    if jd[i]==hd[i]:
        count+=1
print(count)
