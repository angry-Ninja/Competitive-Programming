def hashkey(string):
    ans=0
    for j in range(0,len(string)):
        ans+=ord(string[j])*(j+1)
    return (19*ans)%101

def sort_by_value(dd):
    temp=[]
    for key,value in dd.items():
        temp.append((value,key))
    temp=sorted(temp)
    return temp

for _ in range(int(input())):
    n=int(input())
    d={}
    v=[]
    for j in range(n):
        ll=list(input().split(":"))
        a=ll[0].strip()
        b=ll[1].strip()
        l=[a,b]
        if l[0]=="ADD":
            try:
                d[l[1]]
            except:
                value=hashkey(l[1])
                j=1
                no=value
                while no in v and j<=20:
                    no=(value+j**2+23*j)%101
                    j+=1
                if j<=20:
                    d[l[1]]=no
                    v.append(no)
        else:
             try:
                 val=d[l[1]]
                 del d[l[1]]
                 v.remove(val)
             except:
                 pass
    new_d=sort_by_value(d)
    print(len(new_d))
    for i in new_d:
        print(str(i[0])+":"+i[1])
