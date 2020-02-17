def rep(a):
    if a=="a":
        a=1
    elif a=="b":
        a=2
    elif a=="c":
        a=3
    elif a=="d":
        a=4
    elif a=="e":
        a=5
    elif a=="f":
        a=6
    elif a=="g":
        a=7
    elif a=="h":
        a=8
    return a
x1,y1=list(input())
y1=int(y1)
x1=rep(x1)
x2,y2=list(input())
y2=int(y2)
x2=rep(x2)
steps=0
quarter=0
k=0
ss=[]

while k==0:
    if x2-x1==0 or y2-y1==0:
        k=1
        if x2-x1==0:
            if y2-y1>0:
                st="U"
            else:
                st="D"
        
            steps+=(abs(y2-y1))
            for i in range(abs(y2-y1)):
                ss.append(st)
        elif y2-y1==0:
            if x2-x1>0:
                st="R"
            else:
                st="L"
     
            steps+=(abs(x2-x1))
            for i in range(abs(x2-x1)):
                ss.append(st)
                
    elif x2-x1>0 and y2-y1>0:
        quarter=1
    elif x2-x1>0 and y2-y1<0:
        quarter=2
    elif x2-x1<0 and y2-y1>0:
        quarter=4
    elif x2-x1<0 and y2-y1<0:
        quarter=3
    l=[abs(x2-x1),abs(y2-y1)]
    mm=min(l)
    maxx=max(l)
    if quarter==1:
        for j in range(mm):
            ss.append("RU")
            steps+=1
            x1+=1
            y1+=1
            
        if maxx==mm:
            k=1
    if quarter==2:
        for j in range(mm):
            ss.append("RD")
            steps+=1
            x1+=1
            y1-=1
        if maxx==mm:
            k=1
    if quarter==3:
        for j in range(mm):
            ss.append("LD")
            steps+=1
            x1-=1
            y1-=1
        if maxx==mm:
            k=1
    if quarter==4:
        for j in range(mm):
            ss.append("LU")
            steps+=1
            x1-=1
            y1+=1
        if maxx==mm:
            k=1
print(steps)
for hh in ss:
    print(hh)
