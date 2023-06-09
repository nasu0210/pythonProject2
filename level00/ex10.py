import datetime
import tkinter as tk

def write_diary():
    # 오늘 날짜 가져오기
    today = datetime.date.today()

    # 일기 내용 입력 받기
    diary_content = text_input.get("1.0", "end-1c")

    # 일기 파일에 작성하기
    with open("diary.txt", "a") as file:
        file.write(f"{today}:\n")
        file.write(f"{diary_content}\n")
        file.write("\n")
    text_input.delete("1.0", "end")
    label_status.config(text="일기가 저장되었습니다.")

def read_diary():
    # 일기 파일 읽어오기
    with open("diary.txt", "r") as file:
        diary_entries = file.read()

    # 일기 출력하기
    text_output.delete("1.0", "end")
    text_output.insert("1.0", diary_entries)

# GUI 인터페이스 생성
window = tk.Tk()
window.title("일기장")

# 일기 작성
label_input = tk.Label(window, text="일기 작성:")
label_input.pack()
text_input = tk.Text(window, height=5)
text_input.pack()

button_write = tk.Button(window, text="작성", command=write_diary)
button_write.pack()

# 일기 조회
label_output = tk.Label(window, text="일기 조회:")
label_output.pack()
text_output = tk.Text(window, height=10)
text_output.pack()

button_read = tk.Button(window, text="조회", command=read_diary)
button_read.pack()

# 상태 메시지
label_status = tk.Label(window, text="")
label_status.pack()

# GUI 시작
window.mainloop()
