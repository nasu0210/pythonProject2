import zipfile

# 파일 압축
# with zipfile.ZipFile("c:/data3/archive.zip", "w") as zipf:
#     zipf.write("c:/data3/abc.json")
#     zipf.write("c:/data3/abc_key.json")

# # 파일 압축 해제
with zipfile.ZipFile("c:/data3/archive.zip", "r") as zipf:
    zipf.extractall("c:/data3/aa")
