import serial
import time

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# AT 명령 전송 및 응답 확인 함수
def send_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read_all().decode().strip()
    return response

# SMS 보내기 함수
def send_sms(phone_number, message):
    # SMS 메시지 보내기 AT 명령 전송
    send_command('AT+CMGF=1')  # SMS 텍스트 모드 설정
    send_command('AT+CMGS="{}"'.format(phone_number))  # 수신자 전화번호 설정
    send_command(message)  # 메시지 내용 설정
    ser.write(bytes([26]))  # Ctrl+Z 전송 (메시지 보내기)
    time.sleep(1)
    response = ser.read_all().decode().strip()
    return response

# SMS 보내기
phone_number = '+01090439960'  # 수신자 전화번호를 실제 값으로 대체
message = 'Hello, World!'  # 메시지 내용을 실제 값으로 대체
response = send_sms(phone_number, message)
print(response)

# 시리얼 포트 닫기
ser.close()
