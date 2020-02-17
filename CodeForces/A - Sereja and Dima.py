n=int(input())
l=list(map(int,input().split()))
k=0
summ1=0
summ2=0
for i in range(n):
    if l[0]>l[-1]:
        mm=l[0]
        l=l[1:]
    else:
        mm=l[-1]
        l=l[0:-1]
    if k==0:
        summ1+=mm
        k=1
    else:
        summ2+=mm
        k=0
print(summ1,summ2)
