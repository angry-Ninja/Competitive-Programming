n=int(input())
k=0
s="C."
ss=".C"
s1=s*(n//2)
s2=ss*(n//2)
if n%2==1:
    s1+="C"
    s2+="."
count=0
for i in range(n//2):
    count+=s1.count("C")
    count+=s2.count("C")
if n%2==1:
    count+=s1.count("C")
print(count)
for i in range(n//2):
    print(s1)
    print(s2)
if n%2==1:
    print(s1)
