import cv2
image=cv2.imread('c:/kdata/p001.png')
# 이미지를 블러 처리
image = cv2.blur(image, (20, 20))  # 커널 크기 (5, 5)


cv2.imshow('cat',image)
cv2.waitKey(0)  # 사용자의 키 입력 대기
cv2.destroyAllWindows()  # 창 닫기