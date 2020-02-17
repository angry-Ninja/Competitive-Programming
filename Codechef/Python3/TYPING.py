for m in range(0,int(input())):
    words={}
    
    time=0
    duptime=0
    
    for i in range(0,int(input())):
        newtime=0
        junction=0
        pos=[]
        s=input()
        if s in words:
            duptime+=int(words[s]/2)
        else:    
            for l in s:
                if l=='j' or l=='k':
                    pos.append('R')
                elif l=='d' or l=='f':
                    pos.append('L')
                else:
                    pos.append(" ")
            for k in range(0,len(s)-1):
                if pos[k]==pos[k+1]:
                    junction+=1     
            newtime=(len(s)-junction)*2+junction*4
            time+=newtime
            words[s]=newtime
    print(time+duptime)
