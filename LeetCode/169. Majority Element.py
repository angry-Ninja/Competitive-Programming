class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for j in nums:
            try:
                d[j]+=1
            except:
                d[j]=1
        
        for j in d.keys():
            if d[j]>len(nums)//2:
                return j
            
        
