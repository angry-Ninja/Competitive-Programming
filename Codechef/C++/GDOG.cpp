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
		long long int n,k,i,maxxx=0;
		cin>>n>>k;
		for(i=2;i<=k;i++)
		{
			if(maxxx<(n%i))
			{
				maxxx=n%i;
			}
		}
		cout<<maxxx<<endl;
	}
	return 0;
    
}
