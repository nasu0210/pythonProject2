import cv2
image=cv2.imread('c:/kdata/p001.png')
# 회전 중심점과 회전 각도 설정
center = (image.shape[1] // 2, image.shape[0] // 2)  # 이미지 중심 좌표
angle = 45  # 회전 각도

# 회전 변환 행렬 생성
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)

# 이미지 회전
image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
# 이미지를 블러 처리
image = cv2.blur(image, (20, 20))  # 커널 크기 (5, 5)
cv2.imshow('cat',image)
cv2.waitKey(0)  # 사용자의 키 입력 대기
cv2.destroyAllWindows()  # 창 닫기