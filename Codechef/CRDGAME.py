def summ(n):
    ans=0
    for j in n:
        ans+=int(j)
    return ans
for _ in range(int(input())):
    chef=0
    monty=0
    n=int(input())
    for j in range(n):
        a,b=input().split()
        if summ(a)>summ(b):
            chef+=1
        elif summ(a)<summ(b):
            monty+=1
        else:
            chef+=1
            monty+=1

    if chef>monty:
        print(0,chef)
    elif monty>chef:
        print(1,monty)
    else:
        print(2,chef)
