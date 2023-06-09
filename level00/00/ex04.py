li1=['k_02','k_02','k_03','k_03','k_05']
li2=['m_03','m_02','m_03','m_01','m_03']
li3=li1+li2
print(li3)
li3=[i[-2:] for i in li3]
from collections import Counter
h=Counter(li3)
print(h)


# from collections import defaultdict
# d=defaultdict(int)
# for i in li3:
#     k,v=i.split('_')
#     d[k]+=int(v)
# print(dict(d))