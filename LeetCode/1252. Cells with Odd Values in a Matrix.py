class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        l=[]
        for j in range(n):
            l.append([0]*m)
        
        for j in indices:
            row,col=j[0],j[1]
            for p in range(m):
                l[row][p]+=1
            for p in range(n):
                l[p][col]+=1
        
        count=0
        
        for j in l:
            for k in j:
                if k%2==1:
                    count+=1
        return count
        
                
                
