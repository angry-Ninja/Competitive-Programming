n=int(input())
for i in range(0,n):
    li=input().split()
    li=map(int,li)
    c=0
    flag =1
    for i in li:
        if i==1:
            c+=1
        else:
            c=0
        if c>5:
            flag=0
            print("#coderlifematters")
            break
    if flag==1:
        print("#allcodersarefun")
