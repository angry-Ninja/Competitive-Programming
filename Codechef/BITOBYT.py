for i in range(0,int(input())):
    b=1
    n=0
    B=0
    count=0
    N=int(input())
    while(N>1):
         if count==0:
            if (N//2)>0 and N/2!=1:
                n+=b
                b=0
                N=N-2
                count+=1
            else:
                 break
         else:
              pass
         if count==1:
            if (N//8)>0 and N/8!=1:
                B+=n
                n=0
                N=N-8
                count+=1
            else:
                break
         else:
             pass
                
         if count==2:
             if(N//16)>0 and N/16!=1:
                 b+=B*2
                 B=0
                 N=N-16
                 count+=1
             else:
                 break
         else:
             pass
         if count==3:
            count=0
    print(b,n,B)       
