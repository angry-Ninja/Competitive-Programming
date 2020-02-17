n=int(input())
li=list(map(int,(input().split())))
new1=[]
i=0
sum1=0
prev=li[i]
while i<len(li):
   if prev==li[i]:
       sum1+=li[i]
   else:
        prev=li[i]
        if prev==2:
            new1.append(sum1)
        else:
            new1.append(sum1//2)
        sum1=li[i]   
   i+=1 
if prev==2:
    new1.append(sum1//2)
else:
    new1.append(sum1)


nn=[]        
for i in range(0,len(new1)-1):
    nn.append(min(new1[i+1],new1[i]))
print(max(nn)*2)
