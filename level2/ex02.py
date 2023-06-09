from datetime import datetime, timedelta

def get_date_range_with_weekday(start_date, end_date):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    delta = end - start

    date_list = []
    for i in range(delta.days + 1):
        date = start + timedelta(days=i)
        date_str = date.strftime("%m-%d")
        weekday = date.strftime("%a")  # 요일 구하기
        date_list.append((date_str, weekday))  # 날짜와 요일을 튜플로 리스트에 추가

    return date_list

# 시작일과 종료일 설정
start_date = "2023-04-24"
end_date = "2023-08-25"

# 날짜 범위와 요일 리스트 얻기
date_range_with_weekday = get_date_range_with_weekday(start_date, end_date)
# print(date_range_with_weekday)
date_range_with_weekday = [(date, weekday) for date, weekday in date_range_with_weekday if weekday not in ('Sat', 'Sun')]
print(date_range_with_weekday)
#공휴일 입력
values_to_remove = ['05-01', '05-05','05-29','06-06','08-15']

filtered_list = [(date, weekday) for date, weekday in date_range_with_weekday if date not in values_to_remove]
print(filtered_list)
# 결과 출력
for date, weekday in filtered_list:
    print(date, weekday)
print(dict(filtered_list)['05-03'])

import pandas as pd


# 데이터프레임 생성
df = pd.DataFrame(filtered_list, columns=['Date', 'Weekday'])
df.to_excel('c:/data3/days00.xlsx', index=False)