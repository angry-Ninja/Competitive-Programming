days=[ "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
def days_in_between(d1,d2):
    ind1=days.index(d1)
    ans=1
    while d1!=d2:
        ans+=1
        ind1+=1
        if ind1>6:
            ind1=0
        d1=days[ind1]
    return ans

for i in range(int(input())):
    day1,day2,r1,r2=input().split()
    r1=int(r1)
    r2=int(r2)
    d=days_in_between(day1,day2)
    count=0
    for j in range(d,r2+1,7):
        if j>=r1 and j<=r2:
            count+=1
            if count==1:
                d=j
        if count==2:
            break
    if count==0:
        print("impossible")
    elif count==2:
        print("many")
    else:
        print(d)
