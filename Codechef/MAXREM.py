n=int(input())
l=list(set(map(int, input().split())))
l.sort(reverse=True)
mods=l[1:len(l)+1]
try:
    print(max(mods))
except Exception as e:
    print(0)
