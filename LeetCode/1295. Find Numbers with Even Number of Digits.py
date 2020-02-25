class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for j in nums:
            if len(str(j))%2==0:
                count+=1
        return count
