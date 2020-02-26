class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        i=1
        count=0
        while j<len(nums) and i<len(nums):
            if nums[j]==nums[i]:
                i+=1
            else:
                count+=1
                j=j+1
                nums[j]=nums[i]
        
        return count+1
                
            
