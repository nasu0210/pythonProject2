m=[]
for i in range(10):
    for j in range(10):
        for k in range(10):
            m.append((i,j,k))
print(m)
result = []
visited = set()
for tuple_value in m:
    sorted_tuple = tuple(sorted(tuple_value))
    if sorted_tuple not in visited:
        result.append(tuple_value)
        visited.add(sorted_tuple)
print(result)
print(len(result))



