n=int(input())
l=[]
kk=0
for i in range(n):
    l.append(list(input()))
for j in range(n):
    if kk==1:
        break
    for k in range(n):
        ed=0
  
            #peeche
        if k>0:
            if l[j][k-1]=="o":
                ed+=1
                #aage
        if k+1<=n-1:
            if l[j][k+1]=="o":
                ed+=1
            #upar
        if j-1>=0:
            if l[j-1][k]=="o":
                ed+=1
        if j+1<=n-1:
            if l[j+1][k]=="o":
                ed+=1
        if ed%2==1:
            print("NO")
            kk=1
            break
        else:
            ed=0
            
if kk==0:
    print("YES")
