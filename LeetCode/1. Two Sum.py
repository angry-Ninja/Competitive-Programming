class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictt=dict()
        for j in range(0,len(nums)):
            compliment=target-nums[j]
            if dictt.get(nums[j]) is not None and dictt[nums[j]]!=j:
                return [j,dictt[nums[j]]]
            dictt[compliment]=j
