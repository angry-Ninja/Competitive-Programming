# your code goes here
for i in range(int(input())):
    s1,s2=list(input().split())
    ss1="".join(s1[k] for k in range(len(s1)-1,-1,-1))
    ss2="".join(s2[k] for k in range(len(s2)-1,-1,-1))
    summ=int(ss1)+int(ss2)
    summ=str(summ)
    print(int("".join(summ[h] for h in range(len(summ)-1,-1,-1))))
