def multiply(A,B):
    res=[[0,0],[0,0]]
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                res[i][j]+=(A[i][k]*B[k][j])%1000000007
    return res
 
def fill_partial_results(n,partial_mul):
    for j in range(len(partial_mul),n):
        ans=multiply(partial_mul[-1],partial_mul[-1])
        partial_mul.append(ans)
 
def nthfibbo(n):        #n=power to which matrix need to be raised
    if n==0:
        return 0
    n_bin=bin(n)
    n_bin=n_bin[2:]
    n_bin=n_bin[::-1]
    no_of_partials_needed=len(n_bin)
    fill_partial_results(no_of_partials_needed,partial_mul)
    ANS=[[1,0],[0,1]]
    for j in range(0,len(n_bin)):
        if n_bin[j]=="1":
            ANS=multiply(ANS,partial_mul[j])
    return ANS[0][0]
 
 
partial_mul=[[[1,1],[1,0]]]
for j in range(int(input())):
    x,y=map(int,input().split())
    x=x-1       #n-1 is the power of recurrence relation
    y=y-1
    if x==-1:
        print((nthfibbo(y+2)-1)%1000000007)
    else:
        print((nthfibbo(y+2)%1000000007-nthfibbo(x+1)%1000000007)%1000000007)
 
