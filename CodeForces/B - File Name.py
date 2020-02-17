n=int(input())
s=input()
count=0
l=[]
for i in s:
    if i=='x':
        count+=1
    else:
        if count!=0:
            l.append(count)
            count=0
if s[-1]=="x":
    l.append(count)
rem=0
for j in l:
    if j>2:
        rem+=j-2
print(rem)
