class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        for j in range(0,len(s)//2):
            if s[j]==s[len(s)-j-1]:
                pass
            else:
                return False
        return True
