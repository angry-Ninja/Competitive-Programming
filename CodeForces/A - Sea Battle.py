w1,h1,w2,h2=list(map(int,input().split()))
if w1==w2:
    print(w1+w2+4+h1*2+h2*2)
else:
    if w1>w2:
        print(w1+w2+4+(w1-w2)+h1*2+h2*2)
    else:
        print(w1+w2+4+(w2-w1)+h1*2+h2*2)
