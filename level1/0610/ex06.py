word='Hello world!! happy day!'
word=word.replace('!','').replace(' ','')

a=[]
b=[]
for i in word:
    if i in 'aeiouAEIOU':
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)