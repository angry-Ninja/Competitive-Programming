class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count=0
        for j in range(1,len(points)):
            a,b=abs(points[j][0]-points[j-1][0]),abs(points[j][1]-points[j-1][1])
            minn=min(a,b)
            count+=a+b-minn
        return count
