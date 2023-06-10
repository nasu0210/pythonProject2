import matplotlib.pyplot as plt

# 과일의 이름과 판매량 데이터
fruits = ['사과', '바나나', '딸기', '오렌지']
sales = [30, 40, 25, 35]

# 파이차트 그리기
plt.pie(sales, labels=fruits, autopct='%1.1f%%')

# 파이차트 스타일 설정
plt.axis('equal')  # 파이차트를 원형으로 유지
plt.title('과일 판매량 비율')

# 파이차트 보여주기
plt.show()
