from datetime import datetime, timedelta

s = '2023-05-03'
date = datetime.strptime(s, '%Y-%m-%d')  # 문자열을 날짜로 변환

# 월 증가
date += timedelta(days=1)

# 증가된 날짜를 원하는 형식으로 변환
new_date = date.strftime('%Y-%m-%d')
print(new_date)
