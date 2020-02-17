n,k=list(map(int,input().split()))
odd=0
if n%2==0:
    odd=n//2
else:
    odd=(n//2)+1
if k<=odd :
    print(1+2*(k-1))
else:
   
    print(2+(k-odd-1)*2)
