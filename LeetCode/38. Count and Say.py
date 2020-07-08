class Solution:
    def countAndSay(self, n: int) -> str:
        l=[-3,1]
        for j in range(2,n+1):
            s=str(l[-1])
            inp=""
            i=0
            j=0
            count=0
            while i<len(s) and j<len(s):
                
                if s[i]==s[j]:
                    count+=1
                    j+=1
                
                else:
                    inp=inp+str(count)+str(s[i])
                    count=1
                    i=j
                    j=i+1
            
            inp=inp+str(count)+str(s[i])
            
            l.append((inp))
        return str(l[-1])
                    
                    
                    
        
