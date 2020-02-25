# -> List[int] ====>>return type should be a list
#nums:List[int]====>parameter nums should be of list type
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for j in range(0,len(nums)-1,2):
            for k in range(nums[j]):
                l.append(nums[j+1])
        return l
