for j in range(int(input())):
    n=int(input())
    s=input()
    if "I" in s:
        print("INDIAN")
    elif ("N" in s and "Y" in s) or ("N" not in s and "Y" in s) :
        print("NOT INDIAN")
    else:
        print("NOT SURE")
