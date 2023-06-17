import calendar

# 현재 날짜를 가져옵니다.
import datetime
now = datetime.datetime.now()
year = now.year
month = now.month

# 지정된 연도와 월의 달력을 생성합니다.
cal = calendar.monthcalendar(year, month)

# 달력을 출력합니다.
print(calendar.month_name[month], year)
print(" 월 화 수 목 금 토 일")
for week in cal:
    print(week)

