
klab=['홍길동','김철수','이영희','김민수','이영훈']
eng=[85,75,65,80,60]
kor=[90,80,70,77,56]
li=[]
for name,e,k in zip(klab,eng,kor):
    li.append((name,(e+k)/2))
print(li)
print('-'*50)
a,b=zip(*li)
print(list(a))
print(list(b))