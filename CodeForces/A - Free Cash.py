from collections import Counter 
n=int(input())
l=[]
for i in range(n):
    l.append(input())
d=dict(Counter(l))
print(max(d.values()))
