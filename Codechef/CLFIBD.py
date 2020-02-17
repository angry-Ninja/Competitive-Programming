from collections import Counter
for j in range(0,int(input())):
    s=list(input())
    dic=dict(Counter(s))
    li=list(dic.values())
    li.sort()
  
    length=len(li)
    c=0
    
    
    if len(li)<3:
        print("Dynamic")
    else:
        if li[-1]!=li[-2]+li[-3]:
            c=1
        if c==0:
            print("Dynamic")
        else:
            print("Not")
