ch=list("abcdefghijklmnopqrstuvwxyz")
val=list(range(1,27))
for i in range(int(input())):
    l=[]
    s=input()
    for i in s:
        l.append(val[ch.index(i)])
    if len(list(set(s)))==len(s):

        if max(l)-min(l)-1==len(s)-2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
