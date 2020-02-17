s=input()
s1=input()
s2=""
for i in range(0,len(s1)):
    if s[i]!=s1[i]:
        s2=s2+"1"
    else:
        s2+="0"
print(s2)
