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
    	int x,y,z;
    	cin>>x>>y>>z;
    	if((x+y+z)==180)
    	{
    		cout<<"YES"<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
    return 0;
}
