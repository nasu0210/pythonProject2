letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]
combined_list=[]
for a,b in zip(letters,numbers):
    combined_list.append([a,b])
print(combined_list)