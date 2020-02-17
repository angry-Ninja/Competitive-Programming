#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t>0)
    {
    	t--;
    	int n,m,ans,inp;
    	int k=0;
    	cin>>n>>m;
    	for(int i=0;i<n;i++)
    	{
    		cin>>inp;
    		if(inp%m==0)
    		{
    			k++;
			}
		}
            
			ans=pow(2,k)-1;
			cout<<ans<<endl;  	
	}
    return 0;
}
