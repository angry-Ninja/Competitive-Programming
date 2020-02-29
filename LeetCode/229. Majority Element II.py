class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq=len(nums)//3
        d={}
        l=[]
        for j in nums:
            try:
                if d[j][1]==False:
                    d[j][0]+=1
                    if d[j][0]>freq:
                        l.append(j)
                        d[j][1]=True
            except:
                d[j]=[1,False]
                if d[j][0]>freq:
                    l.append(j)
                    d[j][1]=True
        return l
