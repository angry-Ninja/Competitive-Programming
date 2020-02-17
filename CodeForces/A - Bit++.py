n=int(input())
op=[0,0]
for i in range(n):
    s=input()
    op[0]+=s.count("++")
    op[1]+=s.count("--")
print(op[0]-op[1])
