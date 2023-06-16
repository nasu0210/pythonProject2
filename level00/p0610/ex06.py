import matplotlib.pyplot as plt

tot=[87.5, 77.5, 67.5, 78.5, 58.0]
#kor=[90,80,70,77,56]
klab=['홍길동','김철수','이영희','김민수','이영훈']
plt.rc('font', family='Malgun Gothic') #한글
plt.figure('성적그래프')
k_explode = [0, 0, 0, 0, 0.1]
plt.title('전체 점수')
plt.pie(tot,labels=klab,startangle=0, autopct='%1.2f%%',explode=k_explode)
plt.savefig('c:/data2/score_pie_graph.png')
plt.show()