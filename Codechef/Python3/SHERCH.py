n=int(input())
s=input()
d={"1":"a","2":"bb","3":"ab"}
d1={"a":"b","b":"a"}
string=""
for i in s:
    try:
        string+=d[i]
    except:
        m=""
        for j in string:
            m+=d1[j]
        string=m
print(string)            
