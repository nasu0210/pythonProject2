import matplotlib.pyplot as plt
kor=[90,80,70,77,56]
eng=[85,75,65,80,60]
plt.rc('font', family='Malgun Gothic') #한글
plt.figure('성적그래프')
plt.title('Score')
b_width=0.4
plt.bar(range(5),kor,label='kor',width=b_width)
plt.bar([x+b_width for x in range(5)],eng,label='eng',width=b_width)

plt.xticks([x+b_width/2 for x in range(5)],['홍길동','김철수','이영희','김민수','이영훈'])
plt.yticks(range(0,100,10))
plt.grid()
plt.legend()
plt.savefig('c:/data2/score_graph.png')
plt.show()