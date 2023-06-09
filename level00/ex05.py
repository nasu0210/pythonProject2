import operator

# 리스트 정렬
data = [("John", 25), ("Emily", 30), ("Adam", 18)]
sorted_data = sorted(data, key=operator.itemgetter(0),reverse=False)
print(sorted_data)
