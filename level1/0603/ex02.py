import cv2
image=cv2.imread('c:/kdata/p001.png')
x1, y1 = 0, 0  # 시작 좌표
x2, y2 = 300, 400  # 종료 좌표
image = image[y1:y2, x1:x2]

cv2.imshow('cat',image)
cv2.waitKey(0)  # 사용자의 키 입력 대기
cv2.destroyAllWindows()  # 창 닫기