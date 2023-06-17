li = [6, 1, 2, 3, 2, 4, 5, 10]
c = 0
i = 1
while i < len(li):
    if i != li[c]:
        del li[c]
    else:
        c += 1
        i += 1

print(li)



