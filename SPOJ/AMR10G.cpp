#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t--)
    {
    	int k,i,n;
    	cin>>n>>k;
    	long long int minn=9999999999999;
    	long long int height[n]={0};
    	for(i=0;i<n;i++)
    	{
    		cin>>height[i];
		}
		sort(height,height+n);
	    for(i=0;i<=n-k;i++)
	    {
	    	if(minn>height[i+k-1]-height[i])
	    	{
	    		minn=height[i+k-1]-height[i];
			}
		}
		if(minn==99999999) 
		{
			cout<<height[n-1]-height[0]<<endl;
		}
		else
		{
			cout<<minn<<endl;
		}
	}
    return 0;
}
