for _ in range(int(input())):
    n=int(input())
    cnt=0
    row=99
    col=99
    for i in range(8):
        for j in range(8):
            if i==0 and j==0:
                print("O",end="")
                cnt+=1
                row=0
                col=0
            elif cnt<n:
                print(".",end="")
                cnt=cnt+1
                row=i
                col=j
            elif i==row and j-1==col :
                print("X",end="")
            
            elif i==row and row!=0:
                print("X",end="")
            elif i==row :
                print(".",end="")
            elif i-1==row and j-1<=col:
                print("X",end="")
            else:
                print(".",end="")
        print()
            
