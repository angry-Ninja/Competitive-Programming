from collections import Counter
for _ in range(int(input())):
    s=input()
    l=len(s)
    half=l//2
    if l%2!=0:
        s1=s[:half]
        s2=s[half+1:]
    else:
        s1=s[:half]
        s2=s[half:]
    d1=dict(Counter(s1))
    d2=dict(Counter(s2))
    key1=list(d1.keys())
    key2=list(d2.keys())
    c=0
    if len(key1)==len(key2):
        for k in key1:
            try:
                if d1[k]==d2[k]:
                    pass
                else:
                    c=1
                    break
            except:
                c=1
                break
    else:
        c=1
    if c==0:
        print("YES")
    else:
        print("NO")
