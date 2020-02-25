class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=[0]*len(arr)
        cur_max=arr[-1]
        l[-1]=-1
        for j in range(len(arr)-2,-1,-1):
            
            l[j]=cur_max
            cur_max=max(cur_max,arr[j])
        return l
