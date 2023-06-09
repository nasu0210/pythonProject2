class Event:
    def __init__(self,name,date,time):
        self.name=name
        self.date=date
        self.time=time

class Manager:
    def __init__(self):
        self.li=[]
    def add_event(self,name,date,time):
        event=Event(name,date,time)
        self.li.append(event)
        print("일정이 추가되었습니다.")
    def view_event(self):
        if len(self.li)==0:
            print("등록된 일정이 없습니다.")
        else:
            print("일정 목록:")
            for event in self.li:
                print(f"이름:{event.name}, 날짜:{event.date},시간:{event.time} ")
    def delete_event(self,name):
        for event in self.li:
            if event.name==name:
                self.li.remove(event)
                print("일정이 삭제 되었습니다.")
                return
        print("해당 이름의 일정을 찾을 수 없습니다.")


def main():
    manager=Manager()
    while True:
        print("\n======일정 관리 프로그램 ======")
        print("1. 일정추가")
        print("2. 일정확인")
        print("3. 일정삭제")
        print("4. 종료")
        choice=input("원하는 작업을 선택하세요:")
        if choice=="1":
            name=input("일정을 입력하세요:")
            date=input("날짜를 입력하세요:")
            time=input("시간을 입력하세요:")
            manager.add_event(name,date,time)
        elif choice=="2":
            manager.view_event()
        elif choice=="3":
            name=input('삭제할 일정을 입력하세요:')
            manager.delete_event(name)
        elif choice=="4":
            print("일정 관리 프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택지를 입력하세요.")

main()