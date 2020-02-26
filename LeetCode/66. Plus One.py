class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for j in range(len(digits)-1,-1,-1):
            if digits[j]!=9:
                digits[j]+=1
                break
            elif j==0:
                digits[0]=0
                digits=[1]+digits
            else:
                digits[j]=0
        return digits
