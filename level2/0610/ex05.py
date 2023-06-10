import datetime
d={'월': ['국어', '음악', '영어', '미술', '도덕', '과학'],
'화': ['미술', '가정', '수학', '국어', '과학', '한문', '영어'],
'수': ['기술', '음악', '과학', '체육', '한문', '국어'],
'목': ['도덕', '영어', '과학', '체육', '한문', '가정', '사회'],
'금':['음악', '사회', '도덕', '영어', '체육', '기술']}
day=datetime.date.today()
#day=datetime.date(2023,6,8)
print(day)
weekday=day.weekday()
if weekday in [5,6]:
    print('수업이 없는 요일입니다.')
else:
    weekday_str=['월','화','수','목','금','토','일'][weekday]
    print(d[weekday_str])
