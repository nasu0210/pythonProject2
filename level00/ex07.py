from datetime import datetime, timedelta

s = '2023-05-03'
date = datetime.strptime(s, '%Y-%m-%d')  # 문자열을 날짜로 변환

# 월 증가
year = date.year + (date.month + 1) // 12
month = (date.month + 1) % 12
if month == 0:
    month = 12
day = date.day
new_date = datetime(year, month, day)

# 증가된 날짜를 원하는 형식으로 변환
new_date_str = new_date.strftime('%Y-%m-%d')
print(new_date_str)
