from datetime import datetime, timedelta

def get_date_range(start_date, end_date):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    delta = end - start

    date_list = []
    for i in range(delta.days + 1):
        date = start + timedelta(days=i)
        date_list.append(date.strftime(date_format))

    return date_list

# 시작일과 종료일 설정
start_date = "2023-05-01"
end_date = "2023-05-10"

# 날짜 범위 리스트 얻기
date_range = get_date_range(start_date, end_date)

# 결과 출력
print(date_range)
#
# from datetime import datetime
#
# date_string = "2023-05-01"
# date_format = "%Y-%m-%d"
# date = datetime.strptime(date_string, date_format)
#
# print(date)
