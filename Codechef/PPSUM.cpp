#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int recur(int D,int N)
{
	if(D==0)
	{
		return N;
	}
	else
	{
		N=(N*(N+1))/2;
		return recur(D-1,N);
	}
}

int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t>0)
	{
       t--;	
       int D,N;
       cin>>D>>N;
       int res=recur(D,N);
       cout<<res<<endl;
      
    }
     return 0;
}



