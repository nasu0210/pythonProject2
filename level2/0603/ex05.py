m=[]
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
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
