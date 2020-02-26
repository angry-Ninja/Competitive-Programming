class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)>=3:
            inc=True
            for j in range(0,len(A)-1):
                if A[j]<A[j+1] and inc:
                    pass
                elif A[j]>A[j+1] and not inc:
                    pass
                elif A[j]<A[j+1] and not inc:
                    return False
                elif A[j]>A[j+1] and inc:
                    if j!=0:
                        inc= False
                    else:
                        return False
                elif A[j]==A[j+1]:
                    return False
            if not inc:
                return True
            else:
                return False
        
