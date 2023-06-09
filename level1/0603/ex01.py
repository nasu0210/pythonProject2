import cv2
image=cv2.imread('c:/kdata/p001.png')
x1=0
y1=0
x2=300
y2=300
cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 10)  # 선 그리기
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 10)  # 사각형 그리기
cv2.circle(image, (100, 100), 50, (0, 0, 255), 10)  # 원 그리기
resize=cv2.resize(image,(500,500))
cv2.imshow('cat',resize)
height, width, channels = image.shape
print(f"너비: {width}, 높이: {height}, 채널 수: {channels}")
cv2.imwrite('c:/kdata/output.jpg', image)
cv2.waitKey(0)  # 사용자의 키 입력 대기
cv2.destroyAllWindows()  # 창 닫기