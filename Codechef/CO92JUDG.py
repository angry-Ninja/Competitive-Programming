for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    alice=sum(a)-max(a)
    bob=sum(b)-max(b)
    if alice>bob:
        print("Bob")
    elif bob>alice:
        print("Alice")
    else:
        print("Draw")
            
