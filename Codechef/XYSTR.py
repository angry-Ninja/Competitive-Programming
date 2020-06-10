for _ in range(int(input())):
    s=input()
    count=0
    j=0
    while j<=len(s)-2:
        s1=s[j]+s[j+1]
        if s1=="xy" or s1=="yx":
            count+=1
            j=j+2
        else:
            j=j+1
    print(count)
        
