dd='''
4/24 8
4/25 8
4/26 8
4/27 8
4/28 8
5/2 8
5/3 8
5/4 8
5/8 8
5/9 8
5/10 8
5/11 8
5/12 8
5/15 8
5/16 8
5/17 8
5/18 8
5/19 8
5/22 8
5/23 8
5/24 8
5/25 8
5/26 8
5/30 8
5/31 8
6/1 8
6/2 8
6/5 8
6/7 8
6/8 8
6/9 5
6/12 8
6/13 8
6/14 8
6/15 8
6/16 5
6/19 8
6/20 8
6/21 8
6/22 8
6/23 5
6/26 8
6/27 8
6/28 8
6/29 6
6/30 1
7/3 8
7/4 8
7/5 8
7/6 8
7/7 8
7/10 8
7/11 8
7/12 8
7/13 8
7/14 8
7/17 8
7/18 8
7/19 8
7/20 8
7/21 8
7/24 8
7/25 8
7/26 8
7/27 8
7/28 8
7/31 8
8/1 8
8/2 8
8/3 8
8/4 8
8/7 8
8/8 8
8/9 8
8/10 8
8/11 8
8/14 8
8/16 8
8/17 8
8/18 8
8/21 8
8/22 8
8/23 8
8/24 8
8/25 6
'''
li1=[]
li2=[]
c=0
for i in dd.split():
    if c%2==0:li1.append(i)
    else:li2.append(int(i))
    c+=1
for i,v in enumerate(zip(li1,li2)):
    print(i+1,v)
print(li1)
print(li1.index('5/24'))