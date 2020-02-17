for j in range(int(input())):
    string=input()
    length=len(string)
    c=0
    for j in range(0,length):
        if string[j]!=string[length-j-1]:
            c=1
            break
    if c==0:
        print("YES")
    else:
        print("NO")
