from itertools import permutations
perms = [''.join(p) for p in permutations(['c','h','e','f'])]
for i in range(0,int(input())):
    count=0
    s=input()
    for i in range(0,len(s)-3):
        if s[i:i+4] in perms:
            count+=1
            
    if count>0:
        print("lovely",count)
    else:
        print("normal")
