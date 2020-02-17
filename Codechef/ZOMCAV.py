MAX = 100022

def ranges(C,n):
    s=[]
    e=[]
    b=[]
    for i in range(n):
        r1=i-C[i]
        if r1<0:
            s.append(0)
        else:
            s.append(r1)
        r2=i+C[i]
        if r2>=n:
            e.append(n-1)
        else:
            e.append(r2)
    b.append(s)
    b.append(e)
    return b

def countRanges(L, R, n): 
     
    arr = [0 for i in range(MAX)] 

    for i in range(0, n, 1): 
        arr[L[i]] += 1
        arr[R[i]+1 ] -= 1

    msum = arr[0] 
    for i in range(1, n): 
        arr[i] += arr[i - 1] 
    return arr[:n]


for i in range(int(input())):
    n=int(input())
    C=list(map(int,input().split()))
    H=list(map(int,input().split()))
    rang=ranges(C,n)
    arr=countRanges(rang[0],rang[1],n)
    if sorted(arr)==sorted(H):
        print("YES")
    else:
        print("NO")
