def findTrailingZeros(n):
    count =0
    i=5
    while (n/i>=1):
        count += int(n/i)
        i *= 5
 
    return int(count)
if __name__=="__main__":
    for i in range(0,int(input())):
        print(findTrailingZeros(int(input())))
