d={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
for _ in range(int(input())):
    summ=0
    for i in str(sum(list(map(int,input().split())))):
        summ+=d[int(i)]
    print(summ)
