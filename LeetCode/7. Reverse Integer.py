class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        s=str(x)
        newS=""
        if s[0]=="-":
            neg=True
            s=s[1:]
        for char in s:
            newS=char+newS
        if neg:
            ans= -1*int(newS)
        else:
            ans=int(newS)
        if ans>=-2147483648 and ans<=2147483647:
            return ans
        else:
            return 0
