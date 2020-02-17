def sum(a):
    sum=0
    li=list(a)
    for i in li:
        sum+=int(i)
    print(sum)

if __name__=="__main__":
    n=int(input())
    for i in range(0,n):
        sum(input())
