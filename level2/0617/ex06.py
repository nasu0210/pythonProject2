k=[[0, 0, 63, 99, 89], [0, 0, 89, 0, 0], [0, 92, 63, 99, 0]]
li=list(zip(*k))
result=[]
for i in li:
    result.append(sum(i))
print(result)