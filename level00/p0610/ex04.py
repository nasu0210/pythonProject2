import matplotlib.pyplot as plt
kor=[90,80,70,77,56]
klab=['홍길동','김철수','이영희','김민수','이영훈']
eng=[85,75,65,80,60]
plt.rc('font', family='Malgun Gothic') #한글
plt.figure('성적그래프')
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
k_explode = [0, 0, 0, 0, 0.1]
e_explode = [0.1, 0, 0, 0, 0]
ax1.set_title('국어 점수')
ax1.pie(kor,labels=klab,startangle=0, autopct='%1.2f%%',explode=k_explode)
ax2.set_title('영어 점수')
ax2.pie(eng,labels=klab,startangle=0, autopct='%1.2f%%',explode=e_explode,radius=0.7)
#plt.axis('equal')
plt.savefig('c:/data2/score_pie_graph.png')
plt.show()