A=[]
B=[]
for i in range(0,int(input())):
   
    a,b=list(map(int,input().split()))
    A.append(a)
    B.append(b)
    sumA=sum(A)
    sumB=sum(B)

if sumA%2==0 and sumB%2==0:
    print(0)
elif sumA%2==1 and sumB%2==1 and len(A)!=1:
    k=0
    for j in range(0,len(A)):
        
        if A[j]%2==1 and B[j]%2==0:
            k=1
            print(1)
            break
        elif A[j]%2==0 and B[j]%2==1: 
            k=1
            print(1)
            break
     
    if k==0:
        print(-1)
else:
   print(-1)
