class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        openn=["(","{","["]
        close=[")","}","]"]
        for char in s:
            if char in openn:
                l.append(char)
            if char in close:
                if len(l)!=0 and openn.index(l[-1])==close.index(char):
                    l.pop()
                
                
                else:
                    return False
        if len(l)!=0:
            return False
        else:
            return True
