#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int p;
    cin>>p;
    int res=0;
    if(p%2==0)
    {   int n;
    	n=p/2;
    	if(n%2==1)
    	{
    		res=n/2;
		}
    	else
    	{
    		res=(n/2)-1;
		}
		
	}
	cout<<res<<endl;
    
    return 0;
}
