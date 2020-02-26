class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        if n%2==0:
            for j in range(-(n//2),(n//2)+1):
                if j!=0:
                    l.append(j)
        else:
            for j in range(-(n//2),(n//2)+1):
                l.append(j)
        return l
