s=" "+input()+" "
l=[]
for i in range(0,len(s)):
    if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U" or s[i]==" " or s[i]=="Y":
        l.append(i)
ll=[]
for i in range(1,len(l)):
    ll.append(l[i]-l[i-1])
print(max(ll))
