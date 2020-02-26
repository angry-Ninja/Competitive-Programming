class Solution:
    def romanToInt(self, s: str) -> int:
        dictt={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        summ=0
        cont=False
        for j in range(0,len(s)):
            
            if cont:
                cont=False
                continue
                
            if j!=len(s)-1:
                if s[j]=="I":
                    if s[j+1]=="V":
                        val=4
                        cont=True
                    elif s[j+1]=="X":
                        val=9
                        cont=True                        
                    else:
                        cont=False
                        val=dictt[s[j]]
                elif s[j]=="X":
                    if s[j+1]=="L":
                        val=40
                        cont=True
                    elif s[j+1]=="C":
                        val=90
                        cont=True
                    else:
                        cont=False
                        val=dictt[s[j]]
                elif s[j]=="C":
                    if s[j+1]=="D":
                        val=400
                        cont=True
                    elif s[j+1]=="M":
                        val=900
                        cont=True
                    else:
                        cont=False
                        val=dictt[s[j]]
                else:
                    cont=False
                    val=dictt[s[j]]
                summ+=val
            else:
                cont=False
                summ+=dictt[s[j]]
        return summ
