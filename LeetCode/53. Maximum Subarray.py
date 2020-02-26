class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=0
        maxx=-10e9
        for j in nums:
            curr_max+=j
            if maxx<curr_max:
                maxx=curr_max
            if curr_max<0:
                curr_max=0
        return maxx 
        
