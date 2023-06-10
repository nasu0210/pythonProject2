import matplotlib.pyplot as plt
kor=[90,80,70,77,56]
eng=[85,75,65,80,60]
plt.rc('font', family='Malgun Gothic') #한글
plt.figure('성적그래프')
plt.title('Score')
plt.plot(range(5),kor,label='kor')
plt.scatter(range(5),kor,color='red')
plt.plot(range(5),eng,label='eng')
plt.scatter(range(5),eng,color='green')

plt.xticks(range(5),['홍길동','김철수','이영희','김민수','이영훈'])
plt.grid()
plt.legend()
plt.savefig('c:/data2/score_graph.png')
plt.show()