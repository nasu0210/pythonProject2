word='Hello world!! happy day!'
word=word.replace('!','')
word=word.replace(' ','')
vowels = 'aeiouAEIOU'
a=[]
b=[]
for i in word:
    if i in vowels:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)

