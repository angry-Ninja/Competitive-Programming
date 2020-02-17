t=int(input())

for i in range(t):
    n=int(input())
    s=list(input())
    if n%2==0:
        for i in range(0,n,2):
            k=s[i]
            s[i]=s[i+1]
            s[i+1]=k
    else:
        for i in range(0,n-1,2):
            k=s[i]
            s[i]=s[i+1]
            s[i+1]=k
    
    char=list("abcdefghijklmnopqrstuvwxyz")
    for i in range(0,len(s)):
        l=abs(char.index(s[i])-25)
        s[i]=char[l]
    
    m="".join(s)
    print(m)    
    
