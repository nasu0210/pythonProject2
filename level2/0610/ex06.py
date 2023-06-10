class BusFare:
    def __init__(self):
        self.fare_table = {
            '일반': {'카드': 1250, '현금': 1400},
            '청소년': {'카드': 850, '현금': 1000},
            '어린이': {'카드': 400, '현금': 500}
        }
    def fare(self,age,p_type):
        if age >= 19:  # 일반
            category = '일반'
        elif age >= 13:  # 청소년
            category = '청소년'
        elif age >= 6:  # 어린이
            category = '어린이'
        else:
            return None  # 유효하지 않은 나이일 경우 None 반환
        if p_type in self.fare_table[category]:
            return self.fare_table[category][p_type]
        else:
            return None  # 유효하지 않은 결제 유형일 경우 None 반환

calc=BusFare()
print(calc.fare(25, '카드'))  # 1250
print(calc.fare(15, '현금'))  # 1000
print(calc.fare(8, '카드'))  # 400
print(calc.fare(30, '현금'))  # 1400