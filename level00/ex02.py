from PIL import Image

# 이미지 로드
image = Image.open("c:/data3/sky.png")

# 이미지 크기 변경
resized_image = image.resize((200, 200))

# 이미지 저장
resized_image.save("c:/data3/sky_mall.png")
