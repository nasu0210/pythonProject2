import operator
data=[('홍길동',28,90),('강태욱',15,98),('이수정',14,70),('강태린',12,75)]
sorted_data=sorted(data,key=operator.itemgetter(2),reverse=False)
print(sorted_data)
name,age,score=zip(*data)
print(name)
print(age)
print(score)