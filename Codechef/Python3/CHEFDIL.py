for i  in range(int(input())):
    l=list(input())
    od_ev=l.count("1")
    if od_ev%2==0:
        print("LOSE")
    else:
        print("WIN")
