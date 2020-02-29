class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        for j in range(len(nums)-2,-1,-1):
            if nums[j+1]>nums[j]:
                ind=j
                break
        
        d2=10e9
        ind2=-1
        for j in range(ind+1,len(nums)):
            if nums[ind]<nums[j]:
                d2=min(d2,nums[j])
                ind2=j
        
        nums[ind],nums[ind2]=d2,nums[ind]
        l=[]
        for j in range(ind+1,len(nums)):
            l.append(nums[j])
        
        l.sort()
        i=0
        for j in range(ind+1,len(nums)):
            nums[j]=l[i]
            i+=1
        return nums
        
        
