for i in range(int(input())):
    li=[]
    t=int(input())
    for k in range(0,t):
        li.append(input())
    if t>1:   
        p=set(li[0]).intersection(set(li[1]))
        
        for j in range(2,len(li)):
            p=set(p).intersection(set(li[j]))
         
        print(len(list(p)))
    else:
        print(len(list(set(li[0]))))
