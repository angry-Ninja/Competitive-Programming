def add_1_to_string(num):
    nines=0
    all_nines=True
    length=len(num)
    zeros_to_replace_nines=""
    for j in range(length-1,-1,-1):
        if num[j]=="9":
            nines+=1
            zeros_to_replace_nines+="0"
        else:
            all_nines=False
            break
    if all_nines:
        return "1"+zeros_to_replace_nines
    else:
        digits_not_needed_to_increase=num[:length-nines-1]
        incresed_digit=str(1+int(num[length-nines-1]))
        return digits_not_needed_to_increase+incresed_digit+zeros_to_replace_nines

def nextPalindrome(num):
    length=len(num)
    half=length//2
    isOdd=length%2==1
    if isOdd:
        left=num[:half]
        right=left[::-1]
        middle=num[half]
        pal=left+middle+right
    else:
        left=num[:half-1]
        right=left[::-1]
        middle=num[half-1]
        pal=left+middle+middle+right

    

    if pal>num:
        return pal

    if middle!="9":
        new_middle=str(int(middle)+1)
        if isOdd:
            return left+new_middle+right
        else:
            return left+new_middle+new_middle+right

    else:
        zeros="0"*(half+1)
        newLeft=add_1_to_string(left)
        return nextPalindrome(newLeft+zeros)
        
            
        
    
for j in range(int(input())):
    print(nextPalindrome(input()))
