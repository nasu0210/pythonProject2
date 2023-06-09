# k=660
# m=list(range(1, k+1))
# print(m)
k = 660
# m = []
# for i in range(1, k+1):
#     m.extend([i]*8)
k = 660
m = [i for i in range(1, k+1) for _ in range(8)]

print(m)
