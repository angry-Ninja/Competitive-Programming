for i in range(int(input())):
    s=input()
    print(int("".join(s[x] for x in range(len(s)-1,-1,-1))))
